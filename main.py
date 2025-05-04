#!/usr/bin/env python3

import argparse
import json
import random
import os
from datetime import datetime
from pathlib import Path
import sys


class QuoteGenerator:
    def __init__(self):
        # Built-in quotes database
        self.quotes = {
            "inspirational": [
                {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
                {"quote": "Life is what happens when you're busy making other plans.", "author": "John Lennon"},
                {"quote": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
                {"quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
                {"quote": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
            ],
            "technology": [
                {"quote": "Technology is best when it brings people together.", "author": "Matt Mullenweg"},
                {"quote": "The advance of technology is based on making it fit in so that you don't really even notice it.", "author": "Bill Gates"},
                {"quote": "Any sufficiently advanced technology is indistinguishable from magic.", "author": "Arthur C. Clarke"},
                {"quote": "Code is poetry.", "author": "Anonymous"},
                {"quote": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
            ],
            "programming": [
                {"quote": "Programs must be written for people to read, and only incidentally for machines to execute.", "author": "Harold Abelson"},
                {"quote": "The best way to predict the future is to invent it.", "author": "Alan Kay"},
                {"quote": "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "author": "Martin Fowler"},
                {"quote": "Programming isn't about what you know; it's about what you can figure out.", "author": "Chris Pine"},
                {"quote": "Talk is cheap. Show me the code.", "author": "Linus Torvalds"},
            ],
            "wisdom": [
                {"quote": "In the middle of difficulty lies opportunity.", "author": "Albert Einstein"},
                {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
                {"quote": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
                {"quote": "Everything you've ever wanted is on the other side of fear.", "author": "George Addair"},
                {"quote": "Hardships often prepare ordinary people for an extraordinary destiny.", "author": "C.S. Lewis"},
            ]
        }
        self.custom_quotes_file = "custom_quotes.json"
        self.history_file = ".quote_history.json"
        self.favorites_file = "favorite_quotes.json"
        
        self.load_custom_quotes()
    
    def load_custom_quotes(self):
        """Load custom quotes from file if exists"""
        if os.path.exists(self.custom_quotes_file):
            try:
                with open(self.custom_quotes_file, 'r', encoding='utf-8') as f:
                    custom_quotes = json.load(f)
                    # Merge with built-in quotes
                    for category, quotes in custom_quotes.items():
                        if category in self.quotes:
                            self.quotes[category].extend(quotes)
                        else:
                            self.quotes[category] = quotes
            except Exception as e:
                print(f"Error loading custom quotes: {e}", file=sys.stderr)
    
    def save_to_history(self, quote, author, category):
        """Save viewed quote to history"""
        history = []
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    history = json.load(f)
            except:
                pass
        
        history.append({
            "quote": quote,
            "author": author,
            "category": category,
            "timestamp": datetime.now().isoformat()
        })
        
        # Keep only last 100 quotes
        history = history[-100:]
        
        try:
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(history, f, indent=2)
        except Exception as e:
            print(f"Error saving to history: {e}", file=sys.stderr)
    
    def add_to_favorites(self, quote, author, category):
        """Add quote to favorites"""
        favorites = []
        if os.path.exists(self.favorites_file):
            try:
                with open(self.favorites_file, 'r', encoding='utf-8') as f:
                    favorites = json.load(f)
            except:
                pass
        
        # Check if quote already exists in favorites
        for fav in favorites:
            if fav["quote"] == quote and fav["author"] == author:
                return False
        
        favorites.append({
            "quote": quote,
            "author": author,
            "category": category,
            "saved_at": datetime.now().isoformat()
        })
        
        try:
            with open(self.favorites_file, 'w', encoding='utf-8') as f:
                json.dump(favorites, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving to favorites: {e}", file=sys.stderr)
            return False
    
    def show_quote(self, category=None, random_style=False):
        """Display a random quote"""
        if category:
            if category not in self.quotes:
                available = ", ".join(self.quotes.keys())
                print(f"Category '{category}' not found. Available categories: {available}")
                return None
            
            quotes_list = self.quotes[category]
        else:
            # Get a random category
            category = random.choice(list(self.quotes.keys()))
            quotes_list = self.quotes[category]
        
        if not quotes_list:
            print(f"No quotes found for category '{category}'")
            return None
        
        # Select random quote
        quote_data = random.choice(quotes_list)
        quote = quote_data["quote"]
        author = quote_data["author"]
        
        # Save to history
        self.save_to_history(quote, author, category)
        
        if random_style:
            styles = [self.display_simple, self.display_boxed, self.display_fancy]
            style_func = random.choice(styles)
            style_func(quote, author, category)
        else:
            self.display_simple(quote, author, category)
        
        return quote_data
    
    def display_simple(self, quote, author, category):
        """Display quote in simple format"""
        print(f"\n{quote}")
        print(f"— {author}")
        print(f"Category: {category}\n")
    
    def display_boxed(self, quote, author, category):
        """Display quote in a box"""
        lines = self.wrap_text(quote, 50)
        max_width = max(len(line) for line in lines + [f"— {author}", f"Category: {category}"])
        
        print("\n" + "╭" + "─" * (max_width + 2) + "╮")
        for line in lines:
            print(f"│ {line:<{max_width}} │")
        print(f"│ {'— ' + author:<{max_width}} │")
        print(f"│ {'Category: ' + category:<{max_width}} │")
        print("╰" + "─" * (max_width + 2) + "╯\n")
    
    def display_fancy(self, quote, author, category):
        """Display quote in fancy format"""
        print("\n" + "═" * 60)
        print("  💭  QUOTE OF THE MOMENT")
        print("═" * 60)
        lines = self.wrap_text(f'"{quote}"', 50)
        for line in lines:
            print(f"  {line}")
        print()
        print(f"  — {author}")
        print(f"  📚 Category: {category}")
        print("─" * 60 + "\n")
    
    def wrap_text(self, text, width):
        """Wrap text to specified width"""
        words = text.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + len(current_line) > width:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
            else:
                current_line.append(word)
                current_length += len(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    
    def show_history(self, limit=10):
        """Show quote history"""
        if not os.path.exists(self.history_file):
            print("No history found.")
            return
        
        try:
            with open(self.history_file, 'r', encoding='utf-8') as f:
                history = json.load(f)
        except:
            print("Error reading history.")
            return
        
        print("\n📚 QUOTE HISTORY")
        print("═" * 50)
        
        for item in reversed(history[-limit:]):
            date = datetime.fromisoformat(item["timestamp"]).strftime("%Y-%m-%d %H:%M")
            print(f"[{date}] \"{item['quote']}\" — {item['author']} ({item['category']})")
            print()
    
    def show_favorites(self):
        """Show favorite quotes"""
        if not os.path.exists(self.favorites_file):
            print("No favorite quotes saved.")
            return
        
        try:
            with open(self.favorites_file, 'r', encoding='utf-8') as f:
                favorites = json.load(f)
        except:
            print("Error reading favorites.")
            return
        
        print("\n⭐ FAVORITE QUOTES")
        print("═" * 50)
        
        for i, item in enumerate(favorites, 1):
            print(f"{i}. \"{item['quote']}\"")
            print(f"   — {item['author']} ({item['category']})")
            print(f"   Saved: {datetime.fromisoformat(item['saved_at']).strftime('%Y-%m-%d %H:%M')}")
            print()
    
    def add_custom_quote(self, quote, author, category):
        """Add a custom quote"""
        quotes = []
        if os.path.exists(self.custom_quotes_file):
            try:
                with open(self.custom_quotes_file, 'r', encoding='utf-8') as f:
                    quotes = json.load(f)
            except:
                quotes = {}
        
        if category not in quotes:
            quotes[category] = []
        
        quotes[category].append({"quote": quote, "author": author})
        
        try:
            with open(self.custom_quotes_file, 'w', encoding='utf-8') as f:
                json.dump(quotes, f, indent=2)
            
            # Reload quotes
            self.load_custom_quotes()
            return True
        except Exception as e:
            print(f"Error saving custom quote: {e}")
            return False
    
    def search_quotes(self, keyword):
        """Search quotes by keyword"""
        results = []
        keyword = keyword.lower()
        
        for category, quotes in self.quotes.items():
            for quote_data in quotes:
                quote = quote_data["quote"].lower()
                author = quote_data["author"].lower()
                
                if keyword in quote or keyword in author:
                    results.append({
                        "quote": quote_data["quote"],
                        "author": quote_data["author"],
                        "category": category
                    })
        
        if results:
            print(f"\n🔍 SEARCH RESULTS for '{keyword}'")
            print("═" * 50)
            for result in results:
                print(f"\"{result['quote']}\"")
                print(f"— {result['author']} ({result['category']})")
                print()
        else:
            print(f"No quotes found matching '{keyword}'")
    
    def export_quotes(self, filepath, include_custom=True):
        """Export all quotes to JSON file"""
        export_data = self.quotes.copy() if include_custom else {}
        
        if not include_custom:
            # Exclude custom quotes by loading original file
            if os.path.exists(self.custom_quotes_file):
                try:
                    with open(self.custom_quotes_file, 'r', encoding='utf-8') as f:
                        custom_quotes = json.load(f)
                    
                    # Rebuild built-in quotes dictionary
                    built_in_quotes = {
                        "inspirational": [
                            {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
                            {"quote": "Life is what happens when you're busy making other plans.", "author": "John Lennon"},
                            {"quote": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
                            {"quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
                            {"quote": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
                        ],
                        "technology": [
                            {"quote": "Technology is best when it brings people together.", "author": "Matt Mullenweg"},
                            {"quote": "The advance of technology is based on making it fit in so that you don't really even notice it.", "author": "Bill Gates"},
                            {"quote": "Any sufficiently advanced technology is indistinguishable from magic.", "author": "Arthur C. Clarke"},
                            {"quote": "Code is poetry.", "author": "Anonymous"},
                            {"quote": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
                        ],
                        "programming": [
                            {"quote": "Programs must be written for people to read, and only incidentally for machines to execute.", "author": "Harold Abelson"},
                            {"quote": "The best way to predict the future is to invent it.", "author": "Alan Kay"},
                            {"quote": "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "author": "Martin Fowler"},
                            {"quote": "Programming isn't about what you know; it's about what you can figure out.", "author": "Chris Pine"},
                            {"quote": "Talk is cheap. Show me the code.", "author": "Linus Torvalds"},
                        ],
                        "wisdom": [
                            {"quote": "In the middle of difficulty lies opportunity.", "author": "Albert Einstein"},
                            {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
                            {"quote": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
                            {"quote": "Everything you've ever wanted is on the other side of fear.", "author": "George Addair"},
                            {"quote": "Hardships often prepare ordinary people for an extraordinary destiny.", "author": "C.S. Lewis"},
                        ]
                    }
                    export_data = built_in_quotes
                except:
                    pass
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error exporting quotes: {e}")
            return False


def main():
    parser = argparse.ArgumentParser(description='Random Quote Generator - Get inspired!')
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Random quote command
    random_parser = subparsers.add_parser('random', help='Get a random quote')
    random_parser.add_argument('-c', '--category', help='Specific category')
    random_parser.add_argument('-s', '--style', action='store_true', help='Random display style')
    
    # History commands
    history_parser = subparsers.add_parser('history', help='Show quote history')
    history_parser.add_argument('-n', '--number', type=int, default=10, help='Number of quotes to show')
    
    # Favorites commands
    fav_parser = subparsers.add_parser('favorites', help='Manage favorite quotes')
    fav_parser.add_argument('--show', action='store_true', help='Show favorite quotes')
    fav_parser.add_argument('--add', action='store_true', help='Add last quote to favorites')
    
    # Custom quote commands
    custom_parser = subparsers.add_parser('add', help='Add a custom quote')
    custom_parser.add_argument('quote', help='Quote text')
    custom_parser.add_argument('author', help='Quote author')
    custom_parser.add_argument('-c', '--category', default='custom', help='Quote category')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Search quotes')
    search_parser.add_argument('keyword', help='Search keyword')
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Export quotes to file')
    export_parser.add_argument('filepath', help='Output file path')
    export_parser.add_argument('--no-custom', action='store_true', help='Exclude custom quotes')
    
    # List categories command
    parser.add_argument('--categories', action='store_true', help='List available categories')
    parser.add_argument('--version', action='version', version='Quote Generator v1.0.0')
    
    args = parser.parse_args()
    
    generator = QuoteGenerator()
    
    if args.categories:
        print("Available quote categories:")
        for category in generator.quotes.keys():
            print(f"  - {category}")
        return
    
    if args.command == 'random' or args.command is None:
        # Default to random quote
        quote_data = generator.show_quote(
            category=getattr(args, 'category', None),
            random_style=getattr(args, 'style', False)
        )
        
        if quote_data:
            # Ask if want to add to favorites
            response = input("Add to favorites? (y/n): ").lower()
            if response == 'y':
                if generator.add_to_favorites(quote_data["quote"], quote_data["author"], 
                                            generator.show_quote.__defaults__[0] if getattr(args, 'category', None) is None else args.category):
                    print("Added to favorites! ⭐")
                else:
                    print("Quote already in favorites.")
    
    elif args.command == 'history':
        generator.show_history(args.number)
    
    elif args.command == 'favorites':
        if args.show:
            generator.show_favorites()
    
    elif args.command == 'add':
        if generator.add_custom_quote(args.quote, args.author, args.category):
            print(f"✅ Quote added to category '{args.category}'")
        else:
            print("❌ Failed to add quote")
    
    elif args.command == 'search':
        generator.search_quotes(args.keyword)
    
    elif args.command == 'export':
        if generator.export_quotes(args.filepath, not args.no_custom):
            print(f"✅ Quotes exported to {args.filepath}")
        else:
            print("❌ Failed to export quotes")


if __name__ == "__main__":
    main()
