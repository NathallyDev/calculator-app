import tkinter as tk
from tkinter import messagebox, scrolledtext
import math

# ============================================================
# PALETA DE CORES — Neutros quentes + Verde musgo
# ============================================================
MUSGO_PROFUNDO = "#3D4A2A"
MUSGO_MEDIO    = "#5C6B3E"
MUSGO_CLARO    = "#7A8B5A"
MUSGO_PALIDO   = "#A8B88A"

BEGE_CLARO     = "#FAF8F3"
BEGE_AREIA     = "#F3EFE6"
BEGE_MEDIO     = "#E8E2D3"
CINZA_QUENTE   = "#8B8578"
MARROM_ESCURO  = "#2D2A24"

VERDE_SUCESSO  = "#6B8E4E"
AMBAR_AVISO    = "#C4932B"
TERRACOTA_ERRO = "#A84A3C"

# ============================================================
# ESTADO GLOBAL
# ============================================================
nova_operacao = False
historico = []
modo_radianos = True
memoria = 0.0
tema_escuro = False

# ============================================================
# FUNÇÕES DE LÓGICA
# ============================================================
def clicar_botao(valor):
    global nova_operacao
    if nova_operacao:
        # se o último foi um resultado e o usuário digita um operador,
        # continua a conta; se digita um número, começa nova
        if valor not in ('+', '-', '*', '/', '**', ')', '%'):
            entrada.delete(0, tk.END)
        nova_operacao = False
    entrada.insert(tk.END, str(valor))

def inserir_funcao(func):
    """Insere uma função científica do tipo sin(, cos(, log(, etc."""
    global nova_operacao
    if nova_operacao:
        entrada.delete(0, tk.END)
        nova_operacao = False
    entrada.insert(tk.END, func)

def preprocessar(expr):
    """Converte a expressão visual em expressão Python avaliável."""
    return expr  # Não usado mais

def calcular():
    global nova_operacao, historico
    try:
        expr_original = entrada.get()
        if not expr_original.strip():
            return

        expr = expr_original
        import re
        
        # Tratamentos básicos
        expr = expr.replace('×', '*').replace('X', '*')
        expr = expr.replace('÷', '/')
        expr = expr.replace('−', '-')
        expr = expr.replace('^', '**')
        expr = expr.replace('√(', 'math.sqrt(')
        expr = expr.replace('π', f'({math.pi})')
        expr = expr.replace('φ', f'({(1 + math.sqrt(5)) / 2})')  # phi
        
        # Substituir 'e' isolado
        expr = re.sub(r'(?<![a-zA-Z_])e(?![a-zA-Z_0-9])', f'({math.e})', expr)
        
        # Fatorial
        expr = re.sub(r'(\d+)!', r'math.factorial(\1)', expr)
        
        # Porcentagem
        expr = re.sub(r'(\d+\.?\d*)%', r'(\1/100)', expr)
        
        # Funções trigonométricas
        if modo_radianos:
            expr = expr.replace('sin(', 'math.sin(')
            expr = expr.replace('cos(', 'math.cos(')
            expr = expr.replace('tan(', 'math.tan(')
            expr = expr.replace('asin(', 'math.asin(')
            expr = expr.replace('acos(', 'math.acos(')
            expr = expr.replace('atan(', 'math.atan(')
        else:
            expr = re.sub(r'sin\(', 'math.sin(math.radians(', expr)
            expr = re.sub(r'cos\(', 'math.cos(math.radians(', expr)
            expr = re.sub(r'tan\(', 'math.tan(math.radians(', expr)
            expr = expr.replace('asin(', 'math.degrees(math.asin(')
            expr = expr.replace('acos(', 'math.degrees(math.acos(')
            expr = expr.replace('atan(', 'math.degrees(math.atan(')
        
        # Funções hiperbólicas
        expr = expr.replace('sinh(', 'math.sinh(')
        expr = expr.replace('cosh(', 'math.cosh(')
        expr = expr.replace('tanh(', 'math.tanh(')
        
        # Outras funções
        expr = expr.replace('log(', 'math.log10(')
        expr = expr.replace('ln(', 'math.log(')
        expr = expr.replace('exp(', 'math.exp(')
        expr = expr.replace('abs(', 'abs(')

        # Namespace seguro
        ns = {
            'math': math,
            'abs': abs,
            'round': round,
        }

        resultado = eval(expr, {"__builtins__": {}}, ns)

        # Formatação bonita
        if isinstance(resultado, float):
            if resultado.is_integer():
                resultado_str = str(int(resultado))
            else:
                resultado_str = f"{resultado:.10g}"
        else:
            resultado_str = str(resultado)

        historico.append(f"{expr_original} = {resultado_str}")
        if len(historico) > 30:
            historico.pop(0)

        entrada.delete(0, tk.END)
        entrada.insert(tk.END, resultado_str)
        nova_operacao = True
        
    except ZeroDivisionError:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro: ÷0")
        entrada.config(fg=TERRACOTA_ERRO)
        janela.after(1200, lambda: entrada.config(fg=MARROM_ESCURO))
        nova_operacao = True
    except ValueError as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro: Domínio")
        entrada.config(fg=TERRACOTA_ERRO)
        janela.after(1200, lambda: entrada.config(fg=MARROM_ESCURO))
        nova_operacao = True
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")
        entrada.config(fg=TERRACOTA_ERRO)
        janela.after(1200, lambda: entrada.config(fg=MARROM_ESCURO))
        nova_operacao = True

def limpar():
    entrada.delete(0, tk.END)
    entrada.config(fg=MARROM_ESCURO)

def apagar_ultimo():
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, atual[:-1])

def mostrar_historico():
    if not historico:
        messagebox.showinfo("Histórico", "Nenhuma operação realizada ainda.")
        return
    
    janela_hist = tk.Toplevel(janela)
    janela_hist.title("Histórico de Operações")
    janela_hist.geometry("500x400")
    janela_hist.configure(bg=BEGE_CLARO)
    
    texto_hist = scrolledtext.ScrolledText(
        janela_hist, 
        font=('Segoe UI', 10),
        bg=BEGE_AREIA,
        fg=MARROM_ESCURO,
        wrap=tk.WORD
    )
    texto_hist.pack(fill='both', expand=True, padx=10, pady=10)
    
    for i, item in enumerate(reversed(historico), 1):
        texto_hist.insert(tk.END, f"{i}. {item}\n")
    
    texto_hist.config(state='disabled')
    
    # Botão copiar último
    def copiar_ultimo():
        if historico:
            resultado = historico[-1].split(' = ')[-1]
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, resultado)
    
    btn_copiar = tk.Button(janela_hist, text="📋 Copiar Último", command=copiar_ultimo)
    btn_copiar.pack(pady=5)

def alternar_modo():
    global modo_radianos
    modo_radianos = not modo_radianos
    btn_modo.config(text=f"{'RAD' if modo_radianos else 'DEG'}")
    label_modo.config(text=f"Modo: {'Radianos' if modo_radianos else 'Graus'}")

# Memória
def mem_clear():
    global memoria
    memoria = 0.0
    atualizar_label_memoria()

def mem_recall():
    global nova_operacao
    if nova_operacao:
        entrada.delete(0, tk.END)
        nova_operacao = False
    entrada.insert(tk.END, str(memoria))

def mem_add():
    global memoria
    try:
        memoria += float(entrada.get())
        atualizar_label_memoria()
    except ValueError:
        pass

def mem_sub():
    global memoria
    try:
        memoria -= float(entrada.get())
        atualizar_label_memoria()
    except ValueError:
        pass

def mem_store():
    global memoria
    try:
        memoria = float(entrada.get())
        atualizar_label_memoria()
    except ValueError:
        pass

def atualizar_label_memoria():
    label_memoria.config(text=f"M = {memoria:g}")

# ============================================================
# JANELA PRINCIPAL
# ============================================================
janela = tk.Tk()
janela.title("Calculadora Científica Pro")
janela.configure(bg=BEGE_CLARO)
janela.resizable(False, False)
janela.geometry("900x750")

# Container geral
container = tk.Frame(janela, bg=BEGE_CLARO, padx=20, pady=20)
container.pack(fill='both', expand=True)

# Título
titulo = tk.Label(
    container, text="🧮 Calculadora Científica Pro",
    font=('Segoe UI', 18, 'bold'),
    bg=BEGE_CLARO, fg=MUSGO_PROFUNDO
)
titulo.pack(pady=(0, 10))

# Barra de status
barra_status = tk.Frame(container, bg=BEGE_AREIA, bd=0, relief='flat')
barra_status.pack(fill='x', pady=(0, 8))

label_modo = tk.Label(
    barra_status, text="Modo: Radianos",
    font=('Segoe UI', 9), bg=BEGE_AREIA, fg=CINZA_QUENTE, padx=10, pady=4
)
label_modo.pack(side='left')

label_memoria = tk.Label(
    barra_status, text="M = 0",
    font=('Segoe UI', 9), bg=BEGE_AREIA, fg=CINZA_QUENTE, padx=10, pady=4
)
label_memoria.pack(side='right')

# Visor
visor_frame = tk.Frame(container, bg=BEGE_AREIA, bd=0, highlightthickness=2,
                       highlightbackground=BEGE_MEDIO)
visor_frame.pack(fill='x', pady=(0, 15))

entrada = tk.Entry(
    visor_frame, font=('Segoe UI', 28), borderwidth=0,
    justify='right', bg=BEGE_AREIA, fg=MARROM_ESCURO,
    insertbackground=MUSGO_PROFUNDO
)
entrada.pack(fill='x', padx=15, pady=15, ipady=8)

# ============================================================
# ESTILOS DE BOTÕES
# ============================================================
def criar_botao(parent, texto, comando, estilo='neutro', largura=6):
    """Cria um botão estilizado."""
    estilos = {
        'neutro':    {'bg': BEGE_AREIA,    'fg': MARROM_ESCURO,  'active': BEGE_MEDIO,     'font_w': 'normal'},
        'operador':  {'bg': MUSGO_CLARO,   'fg': BEGE_CLARO,     'active': MUSGO_MEDIO,    'font_w': 'bold'},
        'primario':  {'bg': MUSGO_PROFUNDO,'fg': BEGE_CLARO,     'active': MUSGO_MEDIO,    'font_w': 'bold'},
        'funcao':    {'bg': MUSGO_PALIDO,  'fg': MUSGO_PROFUNDO, 'active': MUSGO_CLARO,    'font_w': 'normal'},
        'perigo':    {'bg': TERRACOTA_ERRO,'fg': BEGE_CLARO,     'active': '#8B3C30',      'font_w': 'bold'},
        'memoria':   {'bg': BEGE_MEDIO,    'fg': MUSGO_PROFUNDO, 'active': MUSGO_PALIDO,   'font_w': 'bold'},
        'toggle':    {'bg': AMBAR_AVISO,   'fg': BEGE_CLARO,     'active': '#A67A1F',      'font_w': 'bold'},
    }
    s = estilos[estilo]
    btn = tk.Button(
        parent, text=texto, command=comando,
        width=largura, height=2,
        font=('Segoe UI', 11, s['font_w']),
        bg=s['bg'], fg=s['fg'],
        activebackground=s['active'], activeforeground=s['fg'],
        relief='flat', bd=0, cursor='hand2',
        highlightthickness=0
    )
    def on_enter(e): btn.config(bg=s['active'])
    def on_leave(e): btn.config(bg=s['bg'])
    btn.bind('<Enter>', on_enter)
    btn.bind('<Leave>', on_leave)
    return btn

# ============================================================
# GRID DE BOTÕES
# ============================================================
grid_frame = tk.Frame(container, bg=BEGE_CLARO)
grid_frame.pack(fill='both', expand=True)

# Linha 0 — Memória + Modo + Histórico
linha0 = tk.Frame(grid_frame, bg=BEGE_CLARO)
linha0.pack(fill='x', pady=(0, 8))

criar_botao(linha0, 'MC', mem_clear, 'memoria').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha0, 'MR', mem_recall, 'memoria').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha0, 'M+', mem_add, 'memoria').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha0, 'M−', mem_sub, 'memoria').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha0, 'MS', mem_store, 'memoria').pack(side='left', padx=2, fill='x', expand=True)
btn_modo = criar_botao(linha0, 'RAD', alternar_modo, 'toggle')
btn_modo.pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha0, 'Hist', mostrar_historico, 'funcao').pack(side='left', padx=2, fill='x', expand=True)

# Linha 1 — Funções trigonométricas básicas
linha1 = tk.Frame(grid_frame, bg=BEGE_CLARO)
linha1.pack(fill='x', pady=(0, 8))

criar_botao(linha1, 'sin', lambda: inserir_funcao('sin('), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha1, 'cos', lambda: inserir_funcao('cos('), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha1, 'tan', lambda: inserir_funcao('tan('), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha1, 'asin', lambda: inserir_funcao('asin('), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha1, 'acos', lambda: inserir_funcao('acos('), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha1, 'atan', lambda: inserir_funcao('atan('), 'funcao').pack(side='left', padx=2, fill='x', expand=True)

# Linha 2 — Funções hiperbólicas + logarítmicas
linha2 = tk.Frame(grid_frame, bg=BEGE_CLARO)
linha2.pack(fill='x', pady=(0, 8))

criar_botao(linha2, 'sinh', lambda: inserir_funcao('sinh('), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha2, 'cosh', lambda: inserir_funcao('cosh('), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha2, 'tanh', lambda: inserir_funcao('tanh('), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha2, 'log', lambda: inserir_funcao('log('), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha2, 'ln', lambda: inserir_funcao('ln('), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha2, 'exp', lambda: inserir_funcao('exp('), 'funcao').pack(side='left', padx=2, fill='x', expand=True)

# Linha 3 — Mais funções
linha3 = tk.Frame(grid_frame, bg=BEGE_CLARO)
linha3.pack(fill='x', pady=(0, 8))

criar_botao(linha3, '√', lambda: inserir_funcao('√('), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha3, 'x²', lambda: clicar_botao('**2'), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha3, 'xʸ', lambda: clicar_botao('**'), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha3, 'x!', lambda: clicar_botao('!'), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha3, '1/x', lambda: inserir_funcao('1/('), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha3, 'abs', lambda: inserir_funcao('abs('), 'funcao').pack(side='left', padx=2, fill='x', expand=True)

# Linha 4 — Constantes
linha4 = tk.Frame(grid_frame, bg=BEGE_CLARO)
linha4.pack(fill='x', pady=(0, 8))

criar_botao(linha4, 'π', lambda: clicar_botao('π'), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha4, 'e', lambda: clicar_botao('e'), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha4, 'φ', lambda: clicar_botao('φ'), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha4, 'C', limpar, 'perigo').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha4, '⌫', apagar_ultimo, 'perigo').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha4, '%', lambda: clicar_botao('%'), 'operador').pack(side='left', padx=2, fill='x', expand=True)

# Linha 5 — Números e operadores (7 8 9)
linha5 = tk.Frame(grid_frame, bg=BEGE_CLARO)
linha5.pack(fill='x', pady=(0, 8))

criar_botao(linha5, '7', lambda: clicar_botao('7'), 'neutro').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha5, '8', lambda: clicar_botao('8'), 'neutro').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha5, '9', lambda: clicar_botao('9'), 'neutro').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha5, '(', lambda: clicar_botao('('), 'operador').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha5, ')', lambda: clicar_botao(')'), 'operador').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha5, '÷', lambda: clicar_botao('/'), 'operador').pack(side='left', padx=2, fill='x', expand=True)

# Linha 6 — Números (4 5 6)
linha6 = tk.Frame(grid_frame, bg=BEGE_CLARO)
linha6.pack(fill='x', pady=(0, 8))

criar_botao(linha6, '4', lambda: clicar_botao('4'), 'neutro').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha6, '5', lambda: clicar_botao('5'), 'neutro').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha6, '6', lambda: clicar_botao('6'), 'neutro').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha6, '×', lambda: clicar_botao('*'), 'operador').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha6, '^', lambda: clicar_botao('**'), 'operador').pack(side='left', padx=2, fill='x', expand=True)
btn_igual_1 = criar_botao(linha6, '=', calcular, 'primario')
btn_igual_1.pack(side='left', padx=2, fill='x', expand=True)

# Linha 7 — Números (1 2 3)
linha7 = tk.Frame(grid_frame, bg=BEGE_CLARO)
linha7.pack(fill='x', pady=(0, 8))

criar_botao(linha7, '1', lambda: clicar_botao('1'), 'neutro').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha7, '2', lambda: clicar_botao('2'), 'neutro').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha7, '3', lambda: clicar_botao('3'), 'neutro').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha7, '−', lambda: clicar_botao('-'), 'operador').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha7, '+', lambda: clicar_botao('+'), 'operador').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha7, '+/−', lambda: clicar_botao('-'), 'operador').pack(side='left', padx=2, fill='x', expand=True)

# Linha 8 — 0 . Ans
linha8 = tk.Frame(grid_frame, bg=BEGE_CLARO)
linha8.pack(fill='x')

btn_zero = criar_botao(linha8, '0', lambda: clicar_botao('0'), 'neutro')
btn_zero.pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha8, '.', lambda: clicar_botao('.'), 'neutro').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha8, 'Ans', lambda: clicar_botao(entrada.get() if nova_operacao else ''), 'funcao').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha8, 'mod', lambda: clicar_botao('%'), 'operador').pack(side='left', padx=2, fill='x', expand=True)
criar_botao(linha8, 'π×', lambda: clicar_botao('*π'), 'funcao').pack(side='left', padx=2, fill='x', expand=True)

# ============================================================
# ATALHOS DE TECLADO
# ============================================================
def tecla_pressionada(event):
    k = event.keysym
    if k == 'Return' or k == 'equal':
        calcular()
    elif k == 'Escape':
        limpar()
    elif k == 'BackSpace':
        apagar_ultimo()

janela.bind('<Key>', tecla_pressionada)
entrada.focus_set()

janela.mainloop()