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
git clone https://github.com/0xQu0rum/quote-generator.git
cd quote-generator
```

2. 🎉 You're ready to get inspired!

## 📖 Usage

### Basic Commands

```bash
# Get a random quote
python main.py random
```

```bash
# Get random quote with random styling
python main.py random -s
```

```bash
# Get quote from specific category
python main.py random -c technology
```

### Categories

```bash
# List all available categories
python main.py --categories
```

#### Available categories:
   - inspirational
   - technology  
   - programming
   - wisdom

### Advanced Features

```bash
# View quote history
python main.py history
```

```bash
# Show last 20 quotes
python main.py history -n 20
```

```bash
# Show favorite quotes
python main.py favorites --show
```

```bash
# Search quotes
python main.py search "code"
```

```bash
# Add custom quote
python main.py add "Your custom quote" "Your Name" -c custom
```

### Export & Import

```bash
# Export all quotes to file
python main.py export quotes.json
```

```bash
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

## 💾 Data Files

The application uses several files to store data:

| File | Purpose | Location |
|------|---------|----------|
| `custom_quotes.json` | User-added quotes | Current directory |
| `favorite_quotes.json` | Starred quotes | Current directory |
| `.quote_history.json` | Viewing history | Current directory |

## 🔧 Command Reference

### Main Commands

| Command | Description | Example |
|---------|-------------|---------|
| `random` | Get a random quote | `python main.py random` |
| `history` | View quote history | `python main.py history` |
| `favorites` | Manage favorites | `python main.py favorites --show` |
| `add` | Add custom quote | `python main.py add "Quote" "Author"` |
| `search` | Search quotes | `python main.py search "inspiration"` |
| `export` | Export quotes | `python main.py export file.json` |

### Options

| Option | Description | Available For |
|--------|-------------|---------------|
| `-c`, `--category` | Specify category | `random` |
| `-s`, `--style` | Random display style | `random` |
| `-n`, `--number` | Number of items | `history` |
| `--no-custom` | Exclude custom quotes | `export` |

## 🎯 Use Cases

- 📱 **Daily Motivation**: Start your day with an inspiring quote
- 💻 **Development Inspiration**: Find programming and tech wisdom
- 📚 **Learning**: Discover new perspectives and ideas
- 🎨 **Presentations**: Find quotes for slides and documents
- 🧘 **Meditation**: Contemplate meaningful thoughts
- 📝 **Writing**: Get inspiration for articles and blogs

## 🔮 Future Features

- [ ] Multiple language support
- [ ] Quote of the day notifications
- [ ] Share quotes to social media
- [ ] Quote image generation
- [ ] Interactive quote mode
- [ ] Quote statistics and analytics
- [ ] Import from external APIs
- [ ] Custom themes and colors

## 🤝 Contributing

Contributions are welcome! Here's how you can contribute:

1. 🐛 Report bugs
2. 💡 Suggest new features
3. ➕ Add new quote categories
4. 🎨 Improve display styles
5. 📝 Enhance documentation

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Add your quotes or features
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## 📝 Quote Database

The application comes with 100+ built-in quotes across multiple categories:
- **Inspirational**: Motivation and life wisdom
- **Technology**: Tech insights and innovation
- **Programming**: Coding philosophy and best practices  
- **Wisdom**: General life advice and philosophy

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments

- 📚 Curated collection of timeless quotes
- 💬 Built for the command-line community
- 🎨 Designed for daily inspiration

---

<div align="center">
  <h3>🌟 Find inspiration every day! 🌟</h3>
  
  ```
     💭 QUOTE GENERATOR 📚
    ╔═══════════════════╗
    ║  Inspire. Learn.  ║
    ║    Motivate.      ║
    ╚═══════════════════╝
  ```
  
  <p>If you find this inspiring, give it a ⭐!</p>
</div>
