# 💬 Random Quote Generator

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Quotes](https://img.shields.io/badge/database-100%2B_quotes-brightgreen.svg)](https://github.com/yourusername/quote-generator)

Get inspired with random quotes from various categories right in your terminal! This CLI tool helps you discover wisdom, motivation, and inspiration with beautiful display styles and powerful features.

```
═══════════════════════════════════════════════════════════════
  💭  QUOTE OF THE MOMENT
═══════════════════════════════════════════════════════════════
  "The only way to do great work is to love what you do."

  — Steve Jobs
  📚 Category: inspirational
───────────────────────────────────────────────────────────────
```

## ✨ Features

- 📚 **Multiple Categories**: Inspirational, Technology, Programming, Wisdom, and more
- 🎨 **Beautiful Display Styles**: Simple, boxed, and fancy formatting options
- ⭐ **Favorites System**: Save and revisit your favorite quotes
- 📝 **Quote History**: Track all viewed quotes with timestamps
- 🔍 **Search Functionality**: Find quotes by keywords
- ➕ **Custom Quotes**: Add your own personal quotes
- 💾 **Import/Export**: Backup and share your quote collection
- 🔄 **Random Styling**: Surprise yourself with different display formats

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/quote-generator.git
cd quote-generator
```

2. 🎉 You're ready to get inspired!

## 📖 Usage

### Basic Commands

```bash
# Get a random quote
python main.py random

# Get random quote with random styling
python main.py random -s

# Get quote from specific category
python main.py random -c technology
```

### Categories

```bash
# List all available categories
python main.py --categories

# Available categories:
#   - inspirational
#   - technology  
#   - programming
#   - wisdom
```

### Advanced Features

```bash
# View quote history
python main.py history

# Show last 20 quotes
python main.py history -n 20

# Show favorite quotes
python main.py favorites --show

# Search quotes
python main.py search "code"

# Add custom quote
python main.py add "Your custom quote" "Your Name" -c custom
```

### Export & Import

```bash
# Export all quotes to file
python main.py export quotes.json

# Export only built-in quotes
python main.py export builtin.json --no-custom
```

## 🎨 Display Styles

The quote generator offers three beautiful display styles:

### 1. Simple Style
```
The best way to predict the future is to invent it.
— Alan Kay
Category: technology
```

### 2. Boxed Style
```
╭───────────────────────────────────────────────────╮
│ Programs must be written for people to read,      │
│ and only incidentally for machines to execute.    │
│ — Harold Abelson                                  │
│ Category: programming                             │
╰───────────────────────────────────────────────────╯
```

### 3. Fancy Style
```
═══════════════════════════════════════════════════════════════
  💭  QUOTE OF THE MOMENT
═══════════════════════════════════════════════════════════════
  "In the middle of difficulty lies opportunity."

  — Albert Einstein
  📚 Category: wisdom
───────────────────────────────────────────────────────────────
```

