# coding: utf-8

import spacy
import textacy.extract

### Load spaCy's English NLP model
nlp = spacy.load('en_core_web_lg')

### The text we want to examine
text = """Dwight Kurt Schrute III (born January 20, 1968) /ˈʃruːt/ is a character on The Office (U.S. TV series). He is one of the highest-ranking salesmen as well as assistant to the regional manager[1] at the paper distribution company Dunder Mifflin, and he is also a bed-and-breakfast proprietor at Schrute Farms, a beet plantation, and as the owner of the business park enclosing Dunder Mifflin. He is notorious for his lack of social skills and common sense, his love for martial arts and the justice system, and his office rivalry with fellow salesman Jim Halpert. He is also known for his romantic relationship with Angela. He has at times risen to the position of acting Branch Manager of the Scranton branch, but often serves as a second or third in command as Assistant to the Regional Manager. In the final season, Dwight is finally offered the position of permanent Regional Manager."""
### Parse the text with spaCy
### Our 'document' variable now contains a parsed version of text.
document = nlp(text)

### print out all the named entities that were detected
for entity in document.ents:
    print(entity.text, entity.label_)
