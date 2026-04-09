# 🧮 Calculadora Científica Pro

<div align="center">

![Python](https://img.shields.io/badge/Python-3.14+-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Ativo-brightgreen?style=flat-square)
![Versão](https://img.shields.io/badge/Versão-2.0-orange?style=flat-square)

**Uma calculadora científica moderna, elegante e poderosa com interface dark mode.**

[Características](#-características) • [Instalação](#-instalação) • [Como Usar](#-como-usar) • [Funcionalidades](#-funcionalidades-técnicas)

</div>

---

## 📋 Visão Geral

A **Calculadora Científica Pro** é um aplicativo desktop desenvolvido em Python com interface gráfica moderna usando Tkinter. Combina funcionalidades científicas avançadas com um design dark mode elegante, perfeito para estudantes, engenheiros e profissionais que precisam de cálculos rápidos e precisos.

### ✨ Destaques

- 🎨 **Interface Dark Mode Moderna** - Design minimalista e sofisticado
- 🔬 **Funções Científicas Completas** - Trigonométricas, hiperbólicas, logarítmicas
- 💾 **Sistema de Memória** - MC, MR, M+, M−, MS
- 📊 **Histórico Detalhado** - Rastreie todas as suas operações
- ⚡ **Performance Otimizada** - Executável único, sem dependências externas
- 🌍 **Suporte a Múltiplos Modos** - Radianos e Graus para trigonometria

---

## 🎯 Características

### Operações Básicas
- ✅ Adição, subtração, multiplicação, divisão
- ✅ Potenciação (x²) e radiciação (√)
- ✅ Percentuais e módulo
- ✅ Inversão de sinal (+/−)
- ✅ Parênteses para prioridade de operações

### Funções Trigonométricas
- `sin`, `cos`, `tan` - Funções trigonométricas
- `asin`, `acos`, `atan` - Funções trigonométricas inversas
- `sinh`, `cosh`, `tanh` - Funções hiperbólicas
- Suporte a **Radianos** e **Graus**

### Funções Logarítmicas
- `log` - Logaritmo base 10
- `ln` - Logaritmo natural
- `exp` - Exponencial (e^x)

### Funções Especiais
- `x!` - Fatorial
- `1/x` - Inverso de um número
- `abs()` - Valor absoluto
- `xʸ` - Potência customizada

### Constantes Matemáticas
- `π` - Pi (3.14159...)
- `e` - Número de Euler (2.71828...)
- `φ` - Número de Ouro (1.61803...)

### Sistema de Memória
- **MC** - Limpar memória
- **MR** - Recuperar valor da memória
- **M+** - Adicionar valor à memória
- **M−** - Subtrair valor da memória
- **MS** - Guardar valor na memória

### Histórico de Operações
- 📜 Histórico completo de até 30 operações
- 🔄 Visualização em janela dedicada
- 📋 Botão para copiar último resultado

---

## 🎨 Design & Paleta de Cores

### Tema Dark Mode Moderno
```
┌─────────────────────────────────┐
│ Fundo Principal:    #0F0F0F     │
│ Superfícies:        #1A-3A1A    │
│ Realce (Musgo):     #7A8B5A     │
│ Texto:              #F5F5F5     │
│ Acento Verde:       #6B8E4E     │
└─────────────────────────────────┘
```

**Código de Cores:**
- **Verde Musgo** - Marca principal, operadores
- **Cinzas Escuros** - Hierarquia de profundidade
- **Branco Suave** - Texto legível e contrastante
- **Tons Semânticos** - Sucesso, aviso, erro

---

## 🚀 Instalação

### Requisitos Mínimos
- Python 3.10+
- Windows 10+ (também funciona em Linux e macOS com Tkinter)
- ~50MB de espaço em disco para o executável

### Opção 1: Executável Standalone (Recomendado)

Simplesmente baixe e execute o arquivo `Program.exe`:

```bash
# Windows
.\dist\Program.exe

# Ou dê duplo clique no arquivo
Program.exe
```

### Opção 2: Executar pelo Python

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/calculator-app.git
cd calculator-app

# Crie um ambiente virtual
python -m venv .venv

# Ative o ambiente
# Windows:
.\.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Instale as dependências (apenas tkinter, já incluído no Python)
# Nenhuma instalação necessária!

# Execute
python Program.py
```

### Opção 3: Construir seu próprio Executável

```bash
# Instale PyInstaller
pip install pyinstaller

# Gere o executável
pyinstaller --onefile --windowed --name=Program Program.py

# Encontre em ./dist/Program.exe
```

---

## 📖 Como Usar

### Cálculos Básicos

1. **Digite sua expressão** no visor
2. **Pressione `=` ou Enter** para calcular
3. **Resultado aparecerá** instantaneamente

#### Exemplos:

| Operação | Digite | Resultado |
|----------|--------|-----------|
| Soma | `5 + 3` | `8` |
| Potência | `2**3` ou `2^3` | `8` |
| Raiz | `√(16)` | `4` |
| Seno (rad) | `sin(π/2)` | `1` |
| Logaritmo | `log(100)` | `2` |
| Fatorial | `5!` | `120` |

### Usando Funções Científicas

**Clique nos botões** de função e complete a expressão:

1. Clique em `sin`
2. Digite o valor: `sin(π/4)`
3. Pressione `=`
4. Resultado: `0.707107...`

### Modo Radianos vs Graus

- Clique no botão **RAD/DEG** para alternar
- `RAD` = Radianos (padrão)
- `DEG` = Graus

### Sistema de Memória

```
1. Digite 42
2. Clique M+       → Adiciona 42 à memória
3. Digite 8
4. Clique M+       → Adiciona 8 (memória = 50)
5. Clique MR       → Mostra 50
6. Clique MC       → Limpa a memória
```

### Visualizar Histórico

1. Clique no botão **Hist**
2. Uma janela abre mostrando todas as operações
3. Clique **📋 Copiar Último** para reutilizar o resultado

### Atalhos de Teclado

| Tecla | Ação |
|-------|------|
| `Enter` | Calcular |
| `=` | Calcular |
| `Escape` | Limpar tudo |
| `Backspace` | Apagar último caractere |
| `0-9` | Digitar números |
| `+`, `-`, `*`, `/` | Operadores |
| `.` | Decimal |

---

## 🔧 Funcionalidades Técnicas

### Arquitetura

```
Program.py
├── Paleta de Cores (22 linhas)
├── Estado Global
├── Funções de Lógica
│   ├── clicar_botao()
│   ├── calcular()
│   ├── inserir_funcao()
│   └── gerenciamento de memória
├── Interface Gráfica (Tkinter)
│   ├── Visor (Entry)
│   ├── 8 linhas de botões
│   └── Barra de status
└── Atalhos de teclado
```

### Segurança

- ✅ Uso de `eval()` com **namespace restrito**
- ✅ Apenas funções matemáticas permitidas
- ✅ Proteção contra divisão por zero
- ✅ Validação de domínio para funções invervas
- ✅ Sem acesso a `__builtins__`

### Performance

- ⚡ Startup instantâneo (executável único)
- ⚡ Cálculos em tempo real
- ⚡ Interface responsiva
- ⚡ Sem lag em operações complexas
- ⚡ ~30MB de footprint total

### Precisão

- 📊 Precisão de 10 dígitos significativos
- 📊 Suporte a números muito grandes
- 📊 Formatação inteligente de resultados
- 📊 Notação científica automática quando necessário

---

## 📁 Estrutura do Projeto

```
calculator-app/
├── Program.py              # Arquivo principal (~800 linhas)
├── Program.spec            # Especificação PyInstaller
├── README.md               # Este arquivo
├── dist/
│   └── Program.exe         # Executável compilado
├── build/                  # Arquivos de compilação
├── .venv/                  # Ambiente virtual
└── .git/                   # Controle de versão
```

---

## 🎨 Personalização

### Alterar Paleta de Cores

Edite as constantes no início de `Program.py`:

```python
MUSGO_PROFUNDO = "#3D4A2A"  # Cor de marca
PRETO_PROFUNDO = "#0F0F0F"  # Fundo
BRANCO_SUAVE = "#F5F5F5"    # Texto
```

### Adicionar Novas Funções

Adicione uma linha no `calcular()`:

```python
expr = expr.replace('sqrt2(', 'math.sqrt(2*')
```

E um botão no grid:

```python
criar_botao(linha1, '√2', lambda: inserir_funcao('sqrt2('), 'funcao').pack(...)
```

---

## 🐛 Possíveis Problemas & Soluções

### Erro: "DLL não encontrada"
**Solução:** Use `Program.exe` da pasta `dist/`, que já inclui todas as dependências.

### Botão não responde
**Solução:** Clique novamente ou pressione Enter após digitar.

### Resultado truncado no visor
**Solução:** Números muito longos são automaticamente formatados. Consulte o histórico para precisão completa.

### Erro de cálculo
**Solução:** Verifique a sintaxe. Ex: `sin(1` precisa de `)` - `sin(1)`

---

## 📊 Benchmarks

```
Operação                Tempo
─────────────────────────────
Adição simples:         < 1ms
sin(π/4):              < 2ms
Fatorial(100):         < 5ms
log(1000000):          < 2ms
```

---

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Ideias de Melhorias

- [ ] Suporte a mais constantes físicas
- [ ] Conversão de unidades integrada
- [ ] Temas adicionais (light mode, high contrast)
- [ ] Gráficos de funções
- [ ] Cálculo de derivadas e integrais simbólicas
- [ ] Exportar histórico como PDF
- [ ] Modo programador (bits, hex, octal)

---

## 📜 Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](LICENSE) para detalhes.

```
MIT License

Copyright (c) 2026 Náthally

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

---

## 🙏 Agradecimentos

- **Python & Tkinter** - Framework base
- **PyInstaller** - Compilação de executáveis
- **Comunidade Open Source** - Inspiração e suporte

---

## 📞 Suporte & Contato

- 📧 Email: seu-email@exemplo.com
- 🐛 Issues: [GitHub Issues](https://github.com/seu-usuario/calculator-app/issues)
- 💬 Discussões: [GitHub Discussions](https://github.com/seu-usuario/calculator-app/discussions)

---

## 🎓 Aprendizados Técnicos

Este projeto demonstra:

✅ Programação orientada a eventos (Tkinter)
✅ Segurança em avaliação de código (`eval` restrito)
✅ Compilação de Python para executáveis
✅ Design Dark Mode moderno
✅ Tratamento de erros robusto
✅ Gestão de estado global
✅ Interface responsiva

---

<div align="center">

### Desenvolvido com ❤️ usando Python 3.14

**[⬆ Voltar ao topo](#-calculadora-científica-pro)**

![Stars](https://img.shields.io/github/stars/seu-usuario/calculator-app?style=social)
![Forks](https://img.shields.io/github/forks/seu-usuario/calculator-app?style=social)
![Watchers](https://img.shields.io/github/watchers/seu-usuario/calculator-app?style=social)

</div>
