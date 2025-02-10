import re
import string
import sys
import argparse

import nltk  # installed by pip install nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def download_nltk_resources():
    nltk.download('punkt')
    nltk.download('stopwords')

def clean_words(text):
    text = text.lower()
    text = re.sub(r'<[^>]+>', ' ', text)  # Remove HTML tags
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    return text

def tokenize_words(text):
    return word_tokenize(text)

def remove_stopwords(tokens, language='english'):
    stop_words = set(stopwords.words(language))  # Use a set for efficiency
    filtered_tokens = list(filter(lambda token: token not in stop_words, tokens)) 
    return filtered_tokens

def stem_tokens(tokens):
    ps = PorterStemmer()
    stemmed_tokens = [ps.stem(token) for token in tokens] # Fixed stemming
    return stemmed_tokens

def process_text(text, remove_stopwords=True, do_stemming=True):
    cleaned = clean_words(text)
    tokens = tokenize_words(cleaned) # Tokenize the cleaned text
    if remove_stopwords:
        tokens = remove_stopwords(tokens)

    if do_stemming:
        tokens = stem_tokens(tokens)

    return tokens

def main():
    parser = argparse.ArgumentParser(description="Clean and process data")
    parser.add_argument('--input', type=str, required=True, help="Path to the input text file.")  # Required input
    parser.add_argument('--output', type=str, help="Path to save the cleaned data (optional). If not provided, the data will print to the console.")
    parser.add_argument('--no-stop', action="store_true", help="Do not remove stop words")
    parser.add_argument('--no-stem', action="store_true", help="Do not perform stemming")

    args = parser.parse_args()

    try:
        with open(args.input, 'r', encoding='utf-8') as infile:
            raw_text = infile.read()
    except FileNotFoundError:
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading the file: {e}", file=sys.stderr)
        sys.exit(1)

    tokens = process_text(raw_text, remove_stopwords=not args.no_stop, do_stemming=not args.no_stem)
    output_text = ' '.join(tokens)

    if args.output:
        try:
            with open(args.output, 'w', encoding="utf-8") as outfile:
                outfile.write(output_text)
            print(f"Processed text written to {args.output}")
        except Exception as e:
            print(f"Error writing output file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print("Cleaned and processed data:")
        print(output_text)


if __name__ == '__main__':
    download_nltk_resources()
    main()


