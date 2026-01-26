"""
Vocabulary Management Module
============================
Add, edit, organize, and import vocabulary cards.

Categories:
    general - General French (travel, conversation, etc.)
    animals - Animal vocabulary

Priority levels (within each category):
    1 - Essential (survival phrases, must-know)
    2 - Very Common (basic travel needs)
    3 - Common (useful travel phrases)
    4 - Helpful (good to know)
    5 - Extra (nice to have)
"""

from database import get_connection


# =============================================================================
# GENERAL FRENCH VOCABULARY
# =============================================================================

GENERAL_VOCABULARY = [
    # =========================================================================
    # PRIORITY 1 - Essential
    # =========================================================================
    {"category": "general", "priority": 1, "topic": "greetings", "french": "Bonjour", "english": "Hello / Good day", "pronunciation": "bohn-ZHOOR"},
    {"category": "general", "priority": 1, "topic": "greetings", "french": "Merci", "english": "Thank you", "pronunciation": "mehr-SEE"},
    {"category": "general", "priority": 1, "topic": "greetings", "french": "S'il vous plaît", "english": "Please", "pronunciation": "seel voo PLEH"},
    {"category": "general", "priority": 1, "topic": "greetings", "french": "Oui", "english": "Yes", "pronunciation": "wee"},
    {"category": "general", "priority": 1, "topic": "greetings", "french": "Non", "english": "No", "pronunciation": "nohn"},
    {"category": "general", "priority": 1, "topic": "greetings", "french": "Pardon", "english": "Sorry / Excuse me", "pronunciation": "pahr-DOHN"},
    {"category": "general", "priority": 1, "topic": "greetings", "french": "Au revoir", "english": "Goodbye", "pronunciation": "oh ruh-VWAHR"},
    {"category": "general", "priority": 1, "topic": "questions", "french": "Parlez-vous anglais?", "english": "Do you speak English?", "pronunciation": "pahr-lay VOO ahn-GLEH"},
    {"category": "general", "priority": 1, "topic": "questions", "french": "Je ne comprends pas", "english": "I don't understand", "pronunciation": "zhuh nuh kohm-PRAHN pah"},
    {"category": "general", "priority": 1, "topic": "questions", "french": "Combien?", "english": "How much?", "pronunciation": "kohm-BYEHN"},
    {"category": "general", "priority": 1, "topic": "questions", "french": "Où est...?", "english": "Where is...?", "pronunciation": "oo EH"},
    {"category": "general", "priority": 1, "topic": "numbers", "french": "Un", "english": "One (1)", "pronunciation": "uhn"},
    {"category": "general", "priority": 1, "topic": "numbers", "french": "Deux", "english": "Two (2)", "pronunciation": "duh"},
    {"category": "general", "priority": 1, "topic": "numbers", "french": "Trois", "english": "Three (3)", "pronunciation": "trwah"},
    {"category": "general", "priority": 1, "topic": "numbers", "french": "Quatre", "english": "Four (4)", "pronunciation": "katr"},
    {"category": "general", "priority": 1, "topic": "numbers", "french": "Cinq", "english": "Five (5)", "pronunciation": "sank"},
    {"category": "general", "priority": 1, "topic": "numbers", "french": "Six", "english": "Six (6)", "pronunciation": "sees"},
    {"category": "general", "priority": 1, "topic": "numbers", "french": "Sept", "english": "Seven (7)", "pronunciation": "set"},
    {"category": "general", "priority": 1, "topic": "numbers", "french": "Huit", "english": "Eight (8)", "pronunciation": "weet"},
    {"category": "general", "priority": 1, "topic": "numbers", "french": "Neuf", "english": "Nine (9)", "pronunciation": "nuhf"},
    {"category": "general", "priority": 1, "topic": "numbers", "french": "Dix", "english": "Ten (10)", "pronunciation": "dees"},
    {"category": "general", "priority": 1, "topic": "emergency", "french": "Aidez-moi!", "english": "Help me!", "pronunciation": "ay-day MWAH"},
    {"category": "general", "priority": 1, "topic": "emergency", "french": "Urgence", "english": "Emergency", "pronunciation": "oor-ZHAHNS"},

    # =========================================================================
    # PRIORITY 2 - Very Common
    # =========================================================================
    {"category": "general", "priority": 2, "topic": "greetings", "french": "Bonsoir", "english": "Good evening", "pronunciation": "bohn-SWAHR"},
    {"category": "general", "priority": 2, "topic": "greetings", "french": "Bonne nuit", "english": "Good night", "pronunciation": "bun NWEE"},
    {"category": "general", "priority": 2, "topic": "greetings", "french": "Salut", "english": "Hi / Bye (informal)", "pronunciation": "sah-LOO"},
    {"category": "general", "priority": 2, "topic": "greetings", "french": "Comment ça va?", "english": "How are you?", "pronunciation": "koh-mohn sah VAH"},
    {"category": "general", "priority": 2, "topic": "greetings", "french": "Ça va bien", "english": "I'm fine", "pronunciation": "sah vah BYEHN"},
    {"category": "general", "priority": 2, "topic": "greetings", "french": "Merci beaucoup", "english": "Thank you very much", "pronunciation": "mehr-SEE boh-KOO"},
    {"category": "general", "priority": 2, "topic": "greetings", "french": "De rien", "english": "You're welcome", "pronunciation": "duh RYEHN"},
    {"category": "general", "priority": 2, "topic": "greetings", "french": "Excusez-moi", "english": "Excuse me (formal)", "pronunciation": "ehk-skoo-zay MWAH"},
    {"category": "general", "priority": 2, "topic": "food", "french": "Je voudrais...", "english": "I would like...", "pronunciation": "zhuh voo-DREH"},
    {"category": "general", "priority": 2, "topic": "food", "french": "L'addition, s'il vous plaît", "english": "The bill, please", "pronunciation": "lah-dee-SYOHN seel voo PLEH"},
    {"category": "general", "priority": 2, "topic": "food", "french": "Un café", "english": "A coffee", "pronunciation": "uhn kah-FAY"},
    {"category": "general", "priority": 2, "topic": "food", "french": "De l'eau", "english": "Water", "pronunciation": "duh LOH"},
    {"category": "general", "priority": 2, "topic": "food", "french": "Une bière", "english": "A beer", "pronunciation": "oon BYEHR"},
    {"category": "general", "priority": 2, "topic": "food", "french": "Du vin", "english": "Wine", "pronunciation": "doo VAHN"},
    {"category": "general", "priority": 2, "topic": "directions", "french": "À gauche", "english": "Left", "pronunciation": "ah GOHSH"},
    {"category": "general", "priority": 2, "topic": "directions", "french": "À droite", "english": "Right", "pronunciation": "ah DRWAHT"},
    {"category": "general", "priority": 2, "topic": "directions", "french": "Tout droit", "english": "Straight ahead", "pronunciation": "too DRWAH"},
    {"category": "general", "priority": 2, "topic": "directions", "french": "Les toilettes", "english": "The toilets", "pronunciation": "lay twah-LET"},
    {"category": "general", "priority": 2, "topic": "numbers", "french": "Onze", "english": "Eleven (11)", "pronunciation": "ohnz"},
    {"category": "general", "priority": 2, "topic": "numbers", "french": "Douze", "english": "Twelve (12)", "pronunciation": "dooz"},
    {"category": "general", "priority": 2, "topic": "numbers", "french": "Treize", "english": "Thirteen (13)", "pronunciation": "trehz"},
    {"category": "general", "priority": 2, "topic": "numbers", "french": "Quatorze", "english": "Fourteen (14)", "pronunciation": "kah-TOHRZ"},
    {"category": "general", "priority": 2, "topic": "numbers", "french": "Quinze", "english": "Fifteen (15)", "pronunciation": "kahnz"},
    {"category": "general", "priority": 2, "topic": "numbers", "french": "Seize", "english": "Sixteen (16)", "pronunciation": "sehz"},
    {"category": "general", "priority": 2, "topic": "numbers", "french": "Dix-sept", "english": "Seventeen (17)", "pronunciation": "dee-SET"},
    {"category": "general", "priority": 2, "topic": "numbers", "french": "Dix-huit", "english": "Eighteen (18)", "pronunciation": "deez-WEET"},
    {"category": "general", "priority": 2, "topic": "numbers", "french": "Dix-neuf", "english": "Nineteen (19)", "pronunciation": "deez-NUHF"},
    {"category": "general", "priority": 2, "topic": "numbers", "french": "Vingt", "english": "Twenty (20)", "pronunciation": "vahn"},
    {"category": "general", "priority": 2, "topic": "questions", "french": "Qu'est-ce que c'est?", "english": "What is this?", "pronunciation": "kess kuh SEH"},
    {"category": "general", "priority": 2, "topic": "questions", "french": "C'est combien?", "english": "How much is it?", "pronunciation": "seh kohm-BYEHN"},
    {"category": "general", "priority": 2, "topic": "questions", "french": "Pourquoi?", "english": "Why?", "pronunciation": "poor-KWAH"},
    {"category": "general", "priority": 2, "topic": "questions", "french": "Quand?", "english": "When?", "pronunciation": "kahn"},
    {"category": "general", "priority": 2, "topic": "questions", "french": "Comment?", "english": "How?", "pronunciation": "koh-MAHN"},

    # =========================================================================
    # PRIORITY 3 - Common
    # =========================================================================
    {"category": "general", "priority": 3, "topic": "food", "french": "Une table pour deux", "english": "A table for two", "pronunciation": "oon TAHBL poor DUH"},
    {"category": "general", "priority": 3, "topic": "food", "french": "Le menu, s'il vous plaît", "english": "The menu, please", "pronunciation": "luh muh-NOO seel voo PLEH"},
    {"category": "general", "priority": 3, "topic": "food", "french": "C'est délicieux", "english": "It's delicious", "pronunciation": "seh day-lee-SYUH"},
    {"category": "general", "priority": 3, "topic": "food", "french": "Un thé", "english": "A tea", "pronunciation": "uhn TAY"},
    {"category": "general", "priority": 3, "topic": "food", "french": "Le petit déjeuner", "english": "Breakfast", "pronunciation": "luh puh-TEE day-zhuh-NAY"},
    {"category": "general", "priority": 3, "topic": "food", "french": "Le déjeuner", "english": "Lunch", "pronunciation": "luh day-zhuh-NAY"},
    {"category": "general", "priority": 3, "topic": "food", "french": "Le dîner", "english": "Dinner", "pronunciation": "luh dee-NAY"},
    {"category": "general", "priority": 3, "topic": "food", "french": "Je suis végétarien(ne)", "english": "I am vegetarian", "pronunciation": "zhuh swee vay-zhay-tah-RYEHN"},
    {"category": "general", "priority": 3, "topic": "food", "french": "Sans gluten", "english": "Gluten-free", "pronunciation": "sahn gloo-TEN"},
    {"category": "general", "priority": 3, "topic": "food", "french": "L'entrée", "english": "Starter/Appetizer", "pronunciation": "lahn-TRAY"},
    {"category": "general", "priority": 3, "topic": "food", "french": "Le plat principal", "english": "Main course", "pronunciation": "luh plah prahn-see-PAHL"},
    {"category": "general", "priority": 3, "topic": "food", "french": "Le dessert", "english": "Dessert", "pronunciation": "luh deh-SEHR"},
    {"category": "general", "priority": 3, "topic": "shopping", "french": "Combien ça coûte?", "english": "How much does it cost?", "pronunciation": "kohm-BYEHN sah KOOT"},
    {"category": "general", "priority": 3, "topic": "shopping", "french": "C'est trop cher", "english": "It's too expensive", "pronunciation": "seh troh SHEHR"},
    {"category": "general", "priority": 3, "topic": "shopping", "french": "Je cherche...", "english": "I'm looking for...", "pronunciation": "zhuh SHEHRSH"},
    {"category": "general", "priority": 3, "topic": "shopping", "french": "Avez-vous...?", "english": "Do you have...?", "pronunciation": "ah-vay VOO"},
    {"category": "general", "priority": 3, "topic": "shopping", "french": "Je peux payer par carte?", "english": "Can I pay by card?", "pronunciation": "zhuh puh pay-YAY pahr KAHRT"},
    {"category": "general", "priority": 3, "topic": "shopping", "french": "En espèces", "english": "In cash", "pronunciation": "ahn ess-PESS"},
    {"category": "general", "priority": 3, "topic": "transport", "french": "La gare", "english": "Train station", "pronunciation": "lah GAHR"},
    {"category": "general", "priority": 3, "topic": "transport", "french": "L'aéroport", "english": "Airport", "pronunciation": "lah-ay-roh-POHR"},
    {"category": "general", "priority": 3, "topic": "transport", "french": "Le métro", "english": "Metro/Subway", "pronunciation": "luh may-TROH"},
    {"category": "general", "priority": 3, "topic": "transport", "french": "Le bus", "english": "Bus", "pronunciation": "luh BOOS"},
    {"category": "general", "priority": 3, "topic": "transport", "french": "Le taxi", "english": "Taxi", "pronunciation": "luh tahk-SEE"},
    {"category": "general", "priority": 3, "topic": "transport", "french": "Un billet", "english": "A ticket", "pronunciation": "uhn bee-YEH"},
    {"category": "general", "priority": 3, "topic": "transport", "french": "Aller-retour", "english": "Round trip", "pronunciation": "ah-lay ruh-TOOR"},
    {"category": "general", "priority": 3, "topic": "transport", "french": "Aller simple", "english": "One way", "pronunciation": "ah-lay SAHM-pluh"},
    {"category": "general", "priority": 3, "topic": "directions", "french": "Près de", "english": "Near", "pronunciation": "preh DUH"},
    {"category": "general", "priority": 3, "topic": "directions", "french": "Loin de", "english": "Far from", "pronunciation": "lwahn DUH"},
    {"category": "general", "priority": 3, "topic": "directions", "french": "La pharmacie", "english": "Pharmacy", "pronunciation": "lah fahr-mah-SEE"},
    {"category": "general", "priority": 3, "topic": "directions", "french": "L'hôpital", "english": "Hospital", "pronunciation": "loh-pee-TAHL"},
    {"category": "general", "priority": 3, "topic": "directions", "french": "La banque", "english": "Bank", "pronunciation": "lah BAHNK"},
    {"category": "general", "priority": 3, "topic": "directions", "french": "Le supermarché", "english": "Supermarket", "pronunciation": "luh soo-pehr-mahr-SHAY"},
    {"category": "general", "priority": 3, "topic": "numbers", "french": "Trente", "english": "Thirty (30)", "pronunciation": "trahnt"},
    {"category": "general", "priority": 3, "topic": "numbers", "french": "Quarante", "english": "Forty (40)", "pronunciation": "kah-RAHNT"},
    {"category": "general", "priority": 3, "topic": "numbers", "french": "Cinquante", "english": "Fifty (50)", "pronunciation": "sahn-KAHNT"},
    {"category": "general", "priority": 3, "topic": "numbers", "french": "Soixante", "english": "Sixty (60)", "pronunciation": "swah-SAHNT"},
    {"category": "general", "priority": 3, "topic": "numbers", "french": "Soixante-dix", "english": "Seventy (70)", "pronunciation": "swah-sahnt DEES"},
    {"category": "general", "priority": 3, "topic": "numbers", "french": "Quatre-vingts", "english": "Eighty (80)", "pronunciation": "katr VAHN"},
    {"category": "general", "priority": 3, "topic": "numbers", "french": "Quatre-vingt-dix", "english": "Ninety (90)", "pronunciation": "katr-vahn DEES"},
    {"category": "general", "priority": 3, "topic": "numbers", "french": "Cent", "english": "One hundred (100)", "pronunciation": "sahn"},
    {"category": "general", "priority": 3, "topic": "emergency", "french": "J'ai besoin d'un médecin", "english": "I need a doctor", "pronunciation": "zhay buh-ZWAHN duhn mayd-SAHN"},
    {"category": "general", "priority": 3, "topic": "emergency", "french": "Appelez la police", "english": "Call the police", "pronunciation": "ah-play lah poh-LEES"},
    {"category": "general", "priority": 3, "topic": "emergency", "french": "Je suis malade", "english": "I am sick", "pronunciation": "zhuh swee mah-LAHD"},
    {"category": "general", "priority": 3, "topic": "emergency", "french": "J'ai perdu mon passeport", "english": "I lost my passport", "pronunciation": "zhay pehr-DOO mohn pahs-POHR"},

    # =========================================================================
    # PRIORITY 4 - Helpful
    # =========================================================================
    {"category": "general", "priority": 4, "topic": "accommodation", "french": "J'ai une réservation", "english": "I have a reservation", "pronunciation": "zhay oon ray-zehr-vah-SYOHN"},
    {"category": "general", "priority": 4, "topic": "accommodation", "french": "Une chambre pour une nuit", "english": "A room for one night", "pronunciation": "oon SHAHM-bruh poor oon NWEE"},
    {"category": "general", "priority": 4, "topic": "accommodation", "french": "Le petit déjeuner est inclus?", "english": "Is breakfast included?", "pronunciation": "luh puh-TEE day-zhuh-NAY eh tahn-KLOO"},
    {"category": "general", "priority": 4, "topic": "accommodation", "french": "À quelle heure est le check-out?", "english": "What time is checkout?", "pronunciation": "ah kel UHR eh luh check-out"},
    {"category": "general", "priority": 4, "topic": "accommodation", "french": "La clé", "english": "The key", "pronunciation": "lah KLAY"},
    {"category": "general", "priority": 4, "topic": "accommodation", "french": "Le wifi", "english": "The wifi", "pronunciation": "luh wee-FEE"},
    {"category": "general", "priority": 4, "topic": "accommodation", "french": "La climatisation", "english": "Air conditioning", "pronunciation": "lah klee-mah-tee-zah-SYOHN"},
    {"category": "general", "priority": 4, "topic": "time", "french": "Quelle heure est-il?", "english": "What time is it?", "pronunciation": "kel UHR eh TEEL"},
    {"category": "general", "priority": 4, "topic": "time", "french": "Aujourd'hui", "english": "Today", "pronunciation": "oh-zhoor-DWEE"},
    {"category": "general", "priority": 4, "topic": "time", "french": "Demain", "english": "Tomorrow", "pronunciation": "duh-MAHN"},
    {"category": "general", "priority": 4, "topic": "time", "french": "Hier", "english": "Yesterday", "pronunciation": "ee-EHR"},
    {"category": "general", "priority": 4, "topic": "time", "french": "Le matin", "english": "Morning", "pronunciation": "luh mah-TAHN"},
    {"category": "general", "priority": 4, "topic": "time", "french": "L'après-midi", "english": "Afternoon", "pronunciation": "lah-preh-mee-DEE"},
    {"category": "general", "priority": 4, "topic": "time", "french": "Le soir", "english": "Evening", "pronunciation": "luh SWAHR"},
    {"category": "general", "priority": 4, "topic": "time", "french": "Maintenant", "english": "Now", "pronunciation": "mahn-tuh-NAHN"},
    {"category": "general", "priority": 4, "topic": "time", "french": "Plus tard", "english": "Later", "pronunciation": "ploo TAHR"},
    {"category": "general", "priority": 4, "topic": "time", "french": "Lundi", "english": "Monday", "pronunciation": "luhn-DEE"},
    {"category": "general", "priority": 4, "topic": "time", "french": "Mardi", "english": "Tuesday", "pronunciation": "mahr-DEE"},
    {"category": "general", "priority": 4, "topic": "time", "french": "Mercredi", "english": "Wednesday", "pronunciation": "mehr-kruh-DEE"},
    {"category": "general", "priority": 4, "topic": "time", "french": "Jeudi", "english": "Thursday", "pronunciation": "zhuh-DEE"},
    {"category": "general", "priority": 4, "topic": "time", "french": "Vendredi", "english": "Friday", "pronunciation": "vahn-druh-DEE"},
    {"category": "general", "priority": 4, "topic": "time", "french": "Samedi", "english": "Saturday", "pronunciation": "sahm-DEE"},
    {"category": "general", "priority": 4, "topic": "time", "french": "Dimanche", "english": "Sunday", "pronunciation": "dee-MAHNSH"},
    {"category": "general", "priority": 4, "topic": "food", "french": "Le pain", "english": "Bread", "pronunciation": "luh PAHN"},
    {"category": "general", "priority": 4, "topic": "food", "french": "Le fromage", "english": "Cheese", "pronunciation": "luh froh-MAHZH"},
    {"category": "general", "priority": 4, "topic": "food", "french": "La viande", "english": "Meat", "pronunciation": "lah VYAHND"},
    {"category": "general", "priority": 4, "topic": "food", "french": "Le poisson", "english": "Fish", "pronunciation": "luh pwah-SOHN"},
    {"category": "general", "priority": 4, "topic": "food", "french": "Les légumes", "english": "Vegetables", "pronunciation": "lay lay-GOOM"},
    {"category": "general", "priority": 4, "topic": "food", "french": "Les fruits", "english": "Fruits", "pronunciation": "lay FRWEE"},
    {"category": "general", "priority": 4, "topic": "food", "french": "Le poulet", "english": "Chicken", "pronunciation": "luh poo-LEH"},
    {"category": "general", "priority": 4, "topic": "food", "french": "Le boeuf", "english": "Beef", "pronunciation": "luh BUHF"},
    {"category": "general", "priority": 4, "topic": "food", "french": "Une salade", "english": "A salad", "pronunciation": "oon sah-LAHD"},
    {"category": "general", "priority": 4, "topic": "food", "french": "Une soupe", "english": "A soup", "pronunciation": "oon SOOP"},
    {"category": "general", "priority": 4, "topic": "adjectives", "french": "Grand(e)", "english": "Big/Tall", "pronunciation": "grahn(d)"},
    {"category": "general", "priority": 4, "topic": "adjectives", "french": "Petit(e)", "english": "Small/Short", "pronunciation": "puh-TEE(t)"},
    {"category": "general", "priority": 4, "topic": "adjectives", "french": "Bon(ne)", "english": "Good", "pronunciation": "bohn(n)"},
    {"category": "general", "priority": 4, "topic": "adjectives", "french": "Mauvais(e)", "english": "Bad", "pronunciation": "moh-VEH(z)"},
    {"category": "general", "priority": 4, "topic": "adjectives", "french": "Chaud(e)", "english": "Hot", "pronunciation": "shoh(d)"},
    {"category": "general", "priority": 4, "topic": "adjectives", "french": "Froid(e)", "english": "Cold", "pronunciation": "frwah(d)"},
    {"category": "general", "priority": 4, "topic": "adjectives", "french": "Ouvert(e)", "english": "Open", "pronunciation": "oo-VEHR(t)"},
    {"category": "general", "priority": 4, "topic": "adjectives", "french": "Fermé(e)", "english": "Closed", "pronunciation": "fehr-MAY"},

    # =========================================================================
    # PRIORITY 5 - Extra
    # =========================================================================
    {"category": "general", "priority": 5, "topic": "weather", "french": "Quel temps fait-il?", "english": "What's the weather like?", "pronunciation": "kel tahn feh TEEL"},
    {"category": "general", "priority": 5, "topic": "weather", "french": "Il fait beau", "english": "It's nice weather", "pronunciation": "eel feh BOH"},
    {"category": "general", "priority": 5, "topic": "weather", "french": "Il fait chaud", "english": "It's hot", "pronunciation": "eel feh SHOH"},
    {"category": "general", "priority": 5, "topic": "weather", "french": "Il fait froid", "english": "It's cold", "pronunciation": "eel feh FRWAH"},
    {"category": "general", "priority": 5, "topic": "weather", "french": "Il pleut", "english": "It's raining", "pronunciation": "eel PLUH"},
    {"category": "general", "priority": 5, "topic": "weather", "french": "Le soleil", "english": "The sun", "pronunciation": "luh soh-LAY"},
    {"category": "general", "priority": 5, "topic": "conversation", "french": "Enchanté(e)", "english": "Nice to meet you", "pronunciation": "ahn-shahn-TAY"},
    {"category": "general", "priority": 5, "topic": "conversation", "french": "Je m'appelle...", "english": "My name is...", "pronunciation": "zhuh mah-PEL"},
    {"category": "general", "priority": 5, "topic": "conversation", "french": "D'où venez-vous?", "english": "Where are you from?", "pronunciation": "doo vuh-nay VOO"},
    {"category": "general", "priority": 5, "topic": "conversation", "french": "Je viens de...", "english": "I come from...", "pronunciation": "zhuh VYEHN duh"},
    {"category": "general", "priority": 5, "topic": "conversation", "french": "Je suis en vacances", "english": "I'm on vacation", "pronunciation": "zhuh swee ahn vah-KAHNS"},
    {"category": "general", "priority": 5, "topic": "conversation", "french": "C'est magnifique!", "english": "It's magnificent!", "pronunciation": "seh mah-nyee-FEEK"},
    {"category": "general", "priority": 5, "topic": "conversation", "french": "Bonne journée!", "english": "Have a good day!", "pronunciation": "bun zhoor-NAY"},
    {"category": "general", "priority": 5, "topic": "conversation", "french": "Bonne soirée!", "english": "Have a good evening!", "pronunciation": "bun swah-RAY"},
    {"category": "general", "priority": 5, "topic": "conversation", "french": "À bientôt!", "english": "See you soon!", "pronunciation": "ah byehn-TOH"},
    {"category": "general", "priority": 5, "topic": "conversation", "french": "Avec plaisir", "english": "With pleasure", "pronunciation": "ah-VEK pleh-ZEER"},
    {"category": "general", "priority": 5, "topic": "phrases", "french": "Je ne sais pas", "english": "I don't know", "pronunciation": "zhuh nuh SEH pah"},
    {"category": "general", "priority": 5, "topic": "phrases", "french": "Pouvez-vous répéter?", "english": "Can you repeat?", "pronunciation": "poo-vay VOO ray-pay-TAY"},
    {"category": "general", "priority": 5, "topic": "phrases", "french": "Plus lentement, s'il vous plaît", "english": "More slowly, please", "pronunciation": "ploo lahnt-MAHN seel voo PLEH"},
    {"category": "general", "priority": 5, "topic": "phrases", "french": "Pouvez-vous m'aider?", "english": "Can you help me?", "pronunciation": "poo-vay VOO meh-DAY"},
    {"category": "general", "priority": 5, "topic": "phrases", "french": "C'est parfait", "english": "It's perfect", "pronunciation": "seh pahr-FEH"},
    {"category": "general", "priority": 5, "topic": "phrases", "french": "Pas de problème", "english": "No problem", "pronunciation": "pah duh proh-BLEM"},
    {"category": "general", "priority": 5, "topic": "phrases", "french": "D'accord", "english": "Okay/Agreed", "pronunciation": "dah-KOHR"},
    {"category": "general", "priority": 5, "topic": "food", "french": "Un jus d'orange", "english": "An orange juice", "pronunciation": "uhn zhoo doh-RAHNZH"},
    {"category": "general", "priority": 5, "topic": "food", "french": "Un verre de vin rouge", "english": "A glass of red wine", "pronunciation": "uhn VEHR duh vahn ROOZH"},
    {"category": "general", "priority": 5, "topic": "food", "french": "Un verre de vin blanc", "english": "A glass of white wine", "pronunciation": "uhn VEHR duh vahn BLAHN"},
    {"category": "general", "priority": 5, "topic": "food", "french": "De l'eau gazeuse", "english": "Sparkling water", "pronunciation": "duh LOH gah-ZUHZ"},
    {"category": "general", "priority": 5, "topic": "food", "french": "De l'eau plate", "english": "Still water", "pronunciation": "duh LOH PLAHT"},
    {"category": "general", "priority": 5, "topic": "shopping", "french": "La taille", "english": "The size", "pronunciation": "lah TIY"},
    {"category": "general", "priority": 5, "topic": "shopping", "french": "Trop grand", "english": "Too big", "pronunciation": "troh GRAHN"},
    {"category": "general", "priority": 5, "topic": "shopping", "french": "Trop petit", "english": "Too small", "pronunciation": "troh puh-TEE"},
    {"category": "general", "priority": 5, "topic": "shopping", "french": "Je regarde seulement", "english": "I'm just looking", "pronunciation": "zhuh ruh-GAHRD suhl-MAHN"},
    {"category": "general", "priority": 5, "topic": "shopping", "french": "C'est en solde?", "english": "Is it on sale?", "pronunciation": "seh tahn SOHLD"},
]


# =============================================================================
# ANIMALS VOCABULARY
# =============================================================================

ANIMALS_VOCABULARY = [
    # =========================================================================
    # PRIORITY 1 - Essential (Common pets & farm animals)
    # =========================================================================
    {"category": "animals", "priority": 1, "topic": "pets", "french": "Le chat", "english": "Cat", "pronunciation": "luh SHAH", "image": "\U0001F431"},
    {"category": "animals", "priority": 1, "topic": "pets", "french": "Le chien", "english": "Dog", "pronunciation": "luh SHYEHN", "image": "\U0001F436"},
    {"category": "animals", "priority": 1, "topic": "farm", "french": "La vache", "english": "Cow", "pronunciation": "lah VAHSH", "image": "\U0001F404"},
    {"category": "animals", "priority": 1, "topic": "farm", "french": "Le cheval", "english": "Horse", "pronunciation": "luh shuh-VAHL", "image": "\U0001F434"},
    {"category": "animals", "priority": 1, "topic": "farm", "french": "Le cochon", "english": "Pig", "pronunciation": "luh koh-SHOHN", "image": "\U0001F437"},
    {"category": "animals", "priority": 1, "topic": "farm", "french": "La poule", "english": "Chicken/Hen", "pronunciation": "lah POOL", "image": "\U0001F414"},
    {"category": "animals", "priority": 1, "topic": "farm", "french": "Le mouton", "english": "Sheep", "pronunciation": "luh moo-TOHN", "image": "\U0001F411"},
    {"category": "animals", "priority": 1, "topic": "general", "french": "L'oiseau", "english": "Bird", "pronunciation": "lwah-ZOH", "image": "\U0001F426"},
    {"category": "animals", "priority": 1, "topic": "general", "french": "Le poisson", "english": "Fish", "pronunciation": "luh pwah-SOHN", "image": "\U0001F41F"},
    {"category": "animals", "priority": 1, "topic": "general", "french": "L'animal", "english": "Animal", "pronunciation": "lah-nee-MAHL", "image": "\U0001F43E"},

    # =========================================================================
    # PRIORITY 2 - Very Common (More pets & farm)
    # =========================================================================
    {"category": "animals", "priority": 2, "topic": "pets", "french": "Le lapin", "english": "Rabbit", "pronunciation": "luh lah-PAHN", "image": "\U0001F430"},
    {"category": "animals", "priority": 2, "topic": "pets", "french": "Le hamster", "english": "Hamster", "pronunciation": "luh ahm-STEHR", "image": "\U0001F439"},
    {"category": "animals", "priority": 2, "topic": "pets", "french": "La tortue", "english": "Turtle/Tortoise", "pronunciation": "lah tohr-TOO", "image": "\U0001F422"},
    {"category": "animals", "priority": 2, "topic": "farm", "french": "Le canard", "english": "Duck", "pronunciation": "luh kah-NAHR", "image": "\U0001F986"},
    {"category": "animals", "priority": 2, "topic": "farm", "french": "L'oie", "english": "Goose", "pronunciation": "LWAH", "image": "\U0001FABF"},
    {"category": "animals", "priority": 2, "topic": "farm", "french": "La chèvre", "english": "Goat", "pronunciation": "lah SHEH-vruh", "image": "\U0001F410"},
    {"category": "animals", "priority": 2, "topic": "farm", "french": "L'âne", "english": "Donkey", "pronunciation": "LAHN", "image": "\U0001FACF"},
    {"category": "animals", "priority": 2, "topic": "farm", "french": "Le coq", "english": "Rooster", "pronunciation": "luh KOHK", "image": "\U0001F413"},
    {"category": "animals", "priority": 2, "topic": "general", "french": "La souris", "english": "Mouse", "pronunciation": "lah soo-REE", "image": "\U0001F401"},
    {"category": "animals", "priority": 2, "topic": "general", "french": "Le rat", "english": "Rat", "pronunciation": "luh RAH", "image": "\U0001F400"},

    # =========================================================================
    # PRIORITY 3 - Common (Wild animals - common)
    # =========================================================================
    {"category": "animals", "priority": 3, "topic": "wild", "french": "Le lion", "english": "Lion", "pronunciation": "luh LYOHN", "image": "\U0001F981"},
    {"category": "animals", "priority": 3, "topic": "wild", "french": "Le tigre", "english": "Tiger", "pronunciation": "luh TEE-gruh", "image": "\U0001F405"},
    {"category": "animals", "priority": 3, "topic": "wild", "french": "L'éléphant", "english": "Elephant", "pronunciation": "lay-lay-FAHN", "image": "\U0001F418"},
    {"category": "animals", "priority": 3, "topic": "wild", "french": "Le singe", "english": "Monkey", "pronunciation": "luh SAHNZH", "image": "\U0001F435"},
    {"category": "animals", "priority": 3, "topic": "wild", "french": "L'ours", "english": "Bear", "pronunciation": "LOORS", "image": "\U0001F43B"},
    {"category": "animals", "priority": 3, "topic": "wild", "french": "Le loup", "english": "Wolf", "pronunciation": "luh LOO", "image": "\U0001F43A"},
    {"category": "animals", "priority": 3, "topic": "wild", "french": "Le renard", "english": "Fox", "pronunciation": "luh ruh-NAHR", "image": "\U0001F98A"},
    {"category": "animals", "priority": 3, "topic": "wild", "french": "Le cerf", "english": "Deer", "pronunciation": "luh SEHR", "image": "\U0001F98C"},
    {"category": "animals", "priority": 3, "topic": "wild", "french": "Le serpent", "english": "Snake", "pronunciation": "luh sehr-PAHN", "image": "\U0001F40D"},
    {"category": "animals", "priority": 3, "topic": "wild", "french": "La girafe", "english": "Giraffe", "pronunciation": "lah zhee-RAHF", "image": "\U0001F992"},
    {"category": "animals", "priority": 3, "topic": "wild", "french": "Le zèbre", "english": "Zebra", "pronunciation": "luh ZEH-bruh", "image": "\U0001F993"},
    {"category": "animals", "priority": 3, "topic": "wild", "french": "Le crocodile", "english": "Crocodile", "pronunciation": "luh kroh-koh-DEEL", "image": "\U0001F40A"},

    # =========================================================================
    # PRIORITY 4 - Helpful (Sea creatures, insects, more wild)
    # =========================================================================
    {"category": "animals", "priority": 4, "topic": "sea", "french": "Le dauphin", "english": "Dolphin", "pronunciation": "luh doh-FAHN", "image": "\U0001F42C"},
    {"category": "animals", "priority": 4, "topic": "sea", "french": "La baleine", "english": "Whale", "pronunciation": "lah bah-LEHN", "image": "\U0001F40B"},
    {"category": "animals", "priority": 4, "topic": "sea", "french": "Le requin", "english": "Shark", "pronunciation": "luh ruh-KAHN", "image": "\U0001F988"},
    {"category": "animals", "priority": 4, "topic": "sea", "french": "La méduse", "english": "Jellyfish", "pronunciation": "lah may-DOOZ", "image": "\U0001FABC"},
    {"category": "animals", "priority": 4, "topic": "sea", "french": "Le crabe", "english": "Crab", "pronunciation": "luh KRAHB", "image": "\U0001F980"},
    {"category": "animals", "priority": 4, "topic": "sea", "french": "La pieuvre", "english": "Octopus", "pronunciation": "lah PYUH-vruh", "image": "\U0001F419"},
    {"category": "animals", "priority": 4, "topic": "insects", "french": "Le papillon", "english": "Butterfly", "pronunciation": "luh pah-pee-YOHN", "image": "\U0001F98B"},
    {"category": "animals", "priority": 4, "topic": "insects", "french": "L'abeille", "english": "Bee", "pronunciation": "lah-BAY", "image": "\U0001F41D"},
    {"category": "animals", "priority": 4, "topic": "insects", "french": "La fourmi", "english": "Ant", "pronunciation": "lah foor-MEE", "image": "\U0001F41C"},
    {"category": "animals", "priority": 4, "topic": "insects", "french": "L'araignée", "english": "Spider", "pronunciation": "lah-reh-NYAY", "image": "\U0001F577\uFE0F"},
    {"category": "animals", "priority": 4, "topic": "wild", "french": "Le kangourou", "english": "Kangaroo", "pronunciation": "luh kahn-goo-ROO", "image": "\U0001F998"},
    {"category": "animals", "priority": 4, "topic": "wild", "french": "Le panda", "english": "Panda", "pronunciation": "luh pahn-DAH", "image": "\U0001F43C"},
    {"category": "animals", "priority": 4, "topic": "wild", "french": "Le koala", "english": "Koala", "pronunciation": "luh koh-ah-LAH", "image": "\U0001F428"},
    {"category": "animals", "priority": 4, "topic": "wild", "french": "Le gorille", "english": "Gorilla", "pronunciation": "luh goh-REE", "image": "\U0001F98D"},

    # =========================================================================
    # PRIORITY 5 - Extra (More animals, animal sounds)
    # =========================================================================
    {"category": "animals", "priority": 5, "topic": "birds", "french": "L'aigle", "english": "Eagle", "pronunciation": "LEH-gluh", "image": "\U0001F985"},
    {"category": "animals", "priority": 5, "topic": "birds", "french": "Le hibou", "english": "Owl", "pronunciation": "luh ee-BOO", "image": "\U0001F989"},
    {"category": "animals", "priority": 5, "topic": "birds", "french": "Le perroquet", "english": "Parrot", "pronunciation": "luh peh-roh-KEH", "image": "\U0001F99C"},
    {"category": "animals", "priority": 5, "topic": "birds", "french": "Le pingouin", "english": "Penguin", "pronunciation": "luh pahn-GWAHN", "image": "\U0001F427"},
    {"category": "animals", "priority": 5, "topic": "wild", "french": "L'hippopotame", "english": "Hippopotamus", "pronunciation": "lee-poh-poh-TAHM", "image": "\U0001F99B"},
    {"category": "animals", "priority": 5, "topic": "wild", "french": "Le rhinocéros", "english": "Rhinoceros", "pronunciation": "luh ree-noh-say-ROHS", "image": "\U0001F98F"},
    {"category": "animals", "priority": 5, "topic": "wild", "french": "Le chameau", "english": "Camel", "pronunciation": "luh shah-MOH", "image": "\U0001F42A"},
    {"category": "animals", "priority": 5, "topic": "wild", "french": "Le léopard", "english": "Leopard", "pronunciation": "luh lay-oh-PAHR", "image": "\U0001F406"},
    {"category": "animals", "priority": 5, "topic": "sounds", "french": "Le chat miaule", "english": "The cat meows", "pronunciation": "luh shah MYOHL"},
    {"category": "animals", "priority": 5, "topic": "sounds", "french": "Le chien aboie", "english": "The dog barks", "pronunciation": "luh shyehn ah-BWAH"},
    {"category": "animals", "priority": 5, "topic": "sounds", "french": "La vache mugit", "english": "The cow moos", "pronunciation": "lah vahsh moo-ZHEE"},
    {"category": "animals", "priority": 5, "topic": "sounds", "french": "Le coq chante", "english": "The rooster crows", "pronunciation": "luh kohk SHAHNT"},
    {"category": "animals", "priority": 5, "topic": "sounds", "french": "L'oiseau chante", "english": "The bird sings", "pronunciation": "lwah-zoh SHAHNT"},
]


# =============================================================================
# COLOURS VOCABULARY (Kid-friendly)
# =============================================================================

COLOURS_VOCABULARY = [
    # =========================================================================
    # PRIORITY 1 - Essential (Basic colours)
    # =========================================================================
    {"category": "colours", "priority": 1, "topic": "basic", "french": "Rouge", "english": "Red", "pronunciation": "ROOZH", "image": "\U0001F534"},
    {"category": "colours", "priority": 1, "topic": "basic", "french": "Bleu", "english": "Blue", "pronunciation": "BLUH", "image": "\U0001F535"},
    {"category": "colours", "priority": 1, "topic": "basic", "french": "Jaune", "english": "Yellow", "pronunciation": "ZHOHN", "image": "\U0001F7E1"},
    {"category": "colours", "priority": 1, "topic": "basic", "french": "Vert", "english": "Green", "pronunciation": "VEHR", "image": "\U0001F7E2"},
    {"category": "colours", "priority": 1, "topic": "basic", "french": "Blanc", "english": "White", "pronunciation": "BLAHN", "image": "\u26AA"},
    {"category": "colours", "priority": 1, "topic": "basic", "french": "Noir", "english": "Black", "pronunciation": "NWAHR", "image": "\u26AB"},
    {"category": "colours", "priority": 1, "topic": "basic", "french": "La couleur", "english": "The colour", "pronunciation": "lah koo-LUHR", "image": "\U0001F3A8"},

    # =========================================================================
    # PRIORITY 2 - Very Common (More colours)
    # =========================================================================
    {"category": "colours", "priority": 2, "topic": "basic", "french": "Orange", "english": "Orange", "pronunciation": "oh-RAHNZH", "image": "\U0001F7E0"},
    {"category": "colours", "priority": 2, "topic": "basic", "french": "Rose", "english": "Pink", "pronunciation": "ROHZ", "image": "\U0001FA77"},
    {"category": "colours", "priority": 2, "topic": "basic", "french": "Violet", "english": "Purple", "pronunciation": "vyoh-LEH", "image": "\U0001F7E3"},
    {"category": "colours", "priority": 2, "topic": "basic", "french": "Marron", "english": "Brown", "pronunciation": "mah-ROHN", "image": "\U0001F7E4"},
    {"category": "colours", "priority": 2, "topic": "basic", "french": "Gris", "english": "Grey", "pronunciation": "GREE", "image": "\U0001F9C3"},
    {"category": "colours", "priority": 2, "topic": "phrases", "french": "De quelle couleur?", "english": "What colour?", "pronunciation": "duh kel koo-LUHR"},

    # =========================================================================
    # PRIORITY 3 - Common (More shades & phrases)
    # =========================================================================
    {"category": "colours", "priority": 3, "topic": "shades", "french": "Bleu clair", "english": "Light blue", "pronunciation": "bluh KLEHR", "image": "\U0001FA75"},
    {"category": "colours", "priority": 3, "topic": "shades", "french": "Bleu foncé", "english": "Dark blue", "pronunciation": "bluh fohn-SAY", "image": "\U0001F4D8"},  # 📘 Blue book
    {"category": "colours", "priority": 3, "topic": "shades", "french": "Vert clair", "english": "Light green", "pronunciation": "vehr KLEHR", "image": "\U0001F33F"},  # 🌿 Herb
    {"category": "colours", "priority": 3, "topic": "shades", "french": "Vert foncé", "english": "Dark green", "pronunciation": "vehr fohn-SAY", "image": "\U0001F332"},  # 🌲 Evergreen
    {"category": "colours", "priority": 3, "topic": "extra", "french": "Or", "english": "Gold", "pronunciation": "OHR", "image": "\U0001F7E1"},
    {"category": "colours", "priority": 3, "topic": "extra", "french": "Argent", "english": "Silver", "pronunciation": "ahr-ZHAHN", "image": "\u26AA"},
    {"category": "colours", "priority": 3, "topic": "phrases", "french": "C'est rouge", "english": "It's red", "pronunciation": "seh ROOZH"},
    {"category": "colours", "priority": 3, "topic": "phrases", "french": "C'est bleu", "english": "It's blue", "pronunciation": "seh BLUH"},

    # =========================================================================
    # PRIORITY 4 - Helpful (Colour descriptions)
    # =========================================================================
    {"category": "colours", "priority": 4, "topic": "extra", "french": "Beige", "english": "Beige", "pronunciation": "BEHZH"},
    {"category": "colours", "priority": 4, "topic": "extra", "french": "Turquoise", "english": "Turquoise", "pronunciation": "toor-KWAHZ", "image": "\U0001FA75"},
    {"category": "colours", "priority": 4, "topic": "extra", "french": "Bordeaux", "english": "Burgundy", "pronunciation": "bohr-DOH"},
    {"category": "colours", "priority": 4, "topic": "phrases", "french": "Le ciel est bleu", "english": "The sky is blue", "pronunciation": "luh syel eh BLUH"},
    {"category": "colours", "priority": 4, "topic": "phrases", "french": "L'herbe est verte", "english": "The grass is green", "pronunciation": "lehrb eh VEHRT"},
    {"category": "colours", "priority": 4, "topic": "phrases", "french": "Le soleil est jaune", "english": "The sun is yellow", "pronunciation": "luh soh-LAY eh ZHOHN"},
    {"category": "colours", "priority": 4, "topic": "phrases", "french": "La neige est blanche", "english": "The snow is white", "pronunciation": "lah nezh eh BLAHNSH"},

    # =========================================================================
    # PRIORITY 5 - Extra (Fun colour phrases)
    # =========================================================================
    {"category": "colours", "priority": 5, "topic": "rainbow", "french": "L'arc-en-ciel", "english": "The rainbow", "pronunciation": "lark-ahn-SYEL", "image": "\U0001F308"},
    {"category": "colours", "priority": 5, "topic": "rainbow", "french": "Les couleurs de l'arc-en-ciel", "english": "Rainbow colours", "pronunciation": "lay koo-LUHR duh lark-ahn-SYEL", "image": "\U0001F308"},
    {"category": "colours", "priority": 5, "topic": "phrases", "french": "Ma couleur préférée", "english": "My favourite colour", "pronunciation": "mah koo-LUHR pray-fay-RAY"},
    {"category": "colours", "priority": 5, "topic": "phrases", "french": "J'aime le bleu", "english": "I like blue", "pronunciation": "zhehm luh BLUH"},
    {"category": "colours", "priority": 5, "topic": "phrases", "french": "La pomme est rouge", "english": "The apple is red", "pronunciation": "lah puhm eh ROOZH"},
    {"category": "colours", "priority": 5, "topic": "phrases", "french": "La banane est jaune", "english": "The banana is yellow", "pronunciation": "lah bah-NAHN eh ZHOHN"},
    {"category": "colours", "priority": 5, "topic": "phrases", "french": "Le chat est noir", "english": "The cat is black", "pronunciation": "luh shah eh NWAHR"},
    {"category": "colours", "priority": 5, "topic": "phrases", "french": "Le chien est marron", "english": "The dog is brown", "pronunciation": "luh shyehn eh mah-ROHN"},
]


# =============================================================================
# BODY PARTS VOCABULARY (Kid-friendly)
# =============================================================================

BODY_PARTS_VOCABULARY = [
    # =========================================================================
    # PRIORITY 1 - Essential (Basic body parts)
    # =========================================================================
    {"category": "body", "priority": 1, "topic": "head", "french": "La tête", "english": "Head", "pronunciation": "lah TET", "image": "\U0001F9D1"},
    {"category": "body", "priority": 1, "topic": "head", "french": "Les yeux", "english": "Eyes", "pronunciation": "layz YUH", "image": "\U0001F440"},
    {"category": "body", "priority": 1, "topic": "head", "french": "Le nez", "english": "Nose", "pronunciation": "luh NAY", "image": "\U0001F443"},
    {"category": "body", "priority": 1, "topic": "head", "french": "La bouche", "english": "Mouth", "pronunciation": "lah BOOSH", "image": "\U0001F444"},
    {"category": "body", "priority": 1, "topic": "head", "french": "Les oreilles", "english": "Ears", "pronunciation": "layz oh-RAY", "image": "\U0001F442"},
    {"category": "body", "priority": 1, "topic": "limbs", "french": "La main", "english": "Hand", "pronunciation": "lah MAHN", "image": "\u270B"},
    {"category": "body", "priority": 1, "topic": "limbs", "french": "Le pied", "english": "Foot", "pronunciation": "luh PYAY", "image": "\U0001F9B6"},

    # =========================================================================
    # PRIORITY 2 - Very Common (More body parts)
    # =========================================================================
    {"category": "body", "priority": 2, "topic": "limbs", "french": "Le bras", "english": "Arm", "pronunciation": "luh BRAH", "image": "\U0001F4AA"},
    {"category": "body", "priority": 2, "topic": "limbs", "french": "La jambe", "english": "Leg", "pronunciation": "lah ZHAHMB", "image": "\U0001F9B5"},
    {"category": "body", "priority": 2, "topic": "head", "french": "Les cheveux", "english": "Hair", "pronunciation": "lay shuh-VUH", "image": "\U0001F9D2"},
    {"category": "body", "priority": 2, "topic": "head", "french": "Le visage", "english": "Face", "pronunciation": "luh vee-ZAHZH", "image": "\U0001F642"},
    {"category": "body", "priority": 2, "topic": "limbs", "french": "Les doigts", "english": "Fingers", "pronunciation": "lay DWAH", "image": "\U0001F446"},
    {"category": "body", "priority": 2, "topic": "limbs", "french": "Les orteils", "english": "Toes", "pronunciation": "layz ohr-TAY", "image": "\U0001F9B6"},
    {"category": "body", "priority": 2, "topic": "body", "french": "Le corps", "english": "Body", "pronunciation": "luh KOHR", "image": "\U0001F9CD"},

    # =========================================================================
    # PRIORITY 3 - Common (More body parts)
    # =========================================================================
    {"category": "body", "priority": 3, "topic": "body", "french": "Le dos", "english": "Back", "pronunciation": "luh DOH"},
    {"category": "body", "priority": 3, "topic": "body", "french": "Le ventre", "english": "Stomach/Belly", "pronunciation": "luh VAHN-truh"},
    {"category": "body", "priority": 3, "topic": "limbs", "french": "L'épaule", "english": "Shoulder", "pronunciation": "lay-POHL"},
    {"category": "body", "priority": 3, "topic": "limbs", "french": "Le genou", "english": "Knee", "pronunciation": "luh zhuh-NOO", "image": "\U0001F9B5"},
    {"category": "body", "priority": 3, "topic": "limbs", "french": "Le coude", "english": "Elbow", "pronunciation": "luh KOOD"},
    {"category": "body", "priority": 3, "topic": "head", "french": "Le cou", "english": "Neck", "pronunciation": "luh KOO"},
    {"category": "body", "priority": 3, "topic": "head", "french": "Les dents", "english": "Teeth", "pronunciation": "lay DAHN", "image": "\U0001F9B7"},
    {"category": "body", "priority": 3, "topic": "head", "french": "La langue", "english": "Tongue", "pronunciation": "lah LAHNG", "image": "\U0001F445"},

    # =========================================================================
    # PRIORITY 4 - Helpful (More parts & simple phrases)
    # =========================================================================
    {"category": "body", "priority": 4, "topic": "head", "french": "Le front", "english": "Forehead", "pronunciation": "luh FROHN"},
    {"category": "body", "priority": 4, "topic": "head", "french": "Le menton", "english": "Chin", "pronunciation": "luh mahn-TOHN"},
    {"category": "body", "priority": 4, "topic": "head", "french": "La joue", "english": "Cheek", "pronunciation": "lah ZHOO"},
    {"category": "body", "priority": 4, "topic": "limbs", "french": "Le pouce", "english": "Thumb", "pronunciation": "luh POOS", "image": "\U0001F44D"},
    {"category": "body", "priority": 4, "topic": "body", "french": "Le coeur", "english": "Heart", "pronunciation": "luh KUHR", "image": "\u2764\uFE0F"},
    {"category": "body", "priority": 4, "topic": "body", "french": "La poitrine", "english": "Chest", "pronunciation": "lah pwah-TREEN"},
    {"category": "body", "priority": 4, "topic": "phrases", "french": "Touche ton nez", "english": "Touch your nose", "pronunciation": "toosh tohn NAY"},
    {"category": "body", "priority": 4, "topic": "phrases", "french": "Touche ta tête", "english": "Touch your head", "pronunciation": "toosh tah TET"},

    # =========================================================================
    # PRIORITY 5 - Extra (Fun action phrases for games)
    # =========================================================================
    {"category": "body", "priority": 5, "topic": "phrases", "french": "Lève les bras", "english": "Raise your arms", "pronunciation": "lev lay BRAH"},
    {"category": "body", "priority": 5, "topic": "phrases", "french": "Tape des mains", "english": "Clap your hands", "pronunciation": "tahp day MAHN"},
    {"category": "body", "priority": 5, "topic": "phrases", "french": "Tape des pieds", "english": "Stomp your feet", "pronunciation": "tahp day PYAY"},
    {"category": "body", "priority": 5, "topic": "phrases", "french": "Ferme les yeux", "english": "Close your eyes", "pronunciation": "fehrm layz YUH"},
    {"category": "body", "priority": 5, "topic": "phrases", "french": "Ouvre la bouche", "english": "Open your mouth", "pronunciation": "oovruh lah BOOSH"},
    {"category": "body", "priority": 5, "topic": "phrases", "french": "Montre-moi tes mains", "english": "Show me your hands", "pronunciation": "mohn-truh MWAH tay MAHN"},
    {"category": "body", "priority": 5, "topic": "phrases", "french": "Secoue la tête", "english": "Shake your head", "pronunciation": "suh-KOO lah TET"},
    {"category": "body", "priority": 5, "topic": "phrases", "french": "Tête, épaules, genoux, pieds", "english": "Head, shoulders, knees, toes", "pronunciation": "tet ay-POHL zhuh-NOO PYAY"},
]


# =============================================================================
# FOOD VOCABULARY (Kid-friendly)
# =============================================================================

FOOD_VOCABULARY = [
    # =========================================================================
    # PRIORITY 1 - Essential (Basic foods kids know)
    # =========================================================================
    {"category": "food_kids", "priority": 1, "topic": "fruit", "french": "La pomme", "english": "Apple", "pronunciation": "lah PUHM", "image": "\U0001F34E"},
    {"category": "food_kids", "priority": 1, "topic": "fruit", "french": "La banane", "english": "Banana", "pronunciation": "lah bah-NAHN", "image": "\U0001F34C"},
    {"category": "food_kids", "priority": 1, "topic": "basics", "french": "Le pain", "english": "Bread", "pronunciation": "luh PAHN", "image": "\U0001F35E"},
    {"category": "food_kids", "priority": 1, "topic": "drinks", "french": "Le lait", "english": "Milk", "pronunciation": "luh LEH", "image": "\U0001F95B"},
    {"category": "food_kids", "priority": 1, "topic": "drinks", "french": "L'eau", "english": "Water", "pronunciation": "LOH", "image": "\U0001F4A7"},
    {"category": "food_kids", "priority": 1, "topic": "basics", "french": "Le fromage", "english": "Cheese", "pronunciation": "luh froh-MAHZH", "image": "\U0001F9C0"},
    {"category": "food_kids", "priority": 1, "topic": "phrases", "french": "J'ai faim", "english": "I'm hungry", "pronunciation": "zhay FAHM"},

    # =========================================================================
    # PRIORITY 2 - Very Common (Popular kid foods)
    # =========================================================================
    {"category": "food_kids", "priority": 2, "topic": "meals", "french": "Le poulet", "english": "Chicken", "pronunciation": "luh poo-LEH", "image": "\U0001F357"},
    {"category": "food_kids", "priority": 2, "topic": "meals", "french": "Les pâtes", "english": "Pasta", "pronunciation": "lay PAHT", "image": "\U0001F35D"},
    {"category": "food_kids", "priority": 2, "topic": "meals", "french": "Le riz", "english": "Rice", "pronunciation": "luh REE", "image": "\U0001F35A"},
    {"category": "food_kids", "priority": 2, "topic": "meals", "french": "La pizza", "english": "Pizza", "pronunciation": "lah peed-ZAH", "image": "\U0001F355"},
    {"category": "food_kids", "priority": 2, "topic": "treats", "french": "La glace", "english": "Ice cream", "pronunciation": "lah GLAHS", "image": "\U0001F368"},
    {"category": "food_kids", "priority": 2, "topic": "treats", "french": "Le gâteau", "english": "Cake", "pronunciation": "luh gah-TOH", "image": "\U0001F370"},
    {"category": "food_kids", "priority": 2, "topic": "phrases", "french": "J'ai soif", "english": "I'm thirsty", "pronunciation": "zhay SWAHF"},

    # =========================================================================
    # PRIORITY 3 - Common (Fruits & vegetables)
    # =========================================================================
    {"category": "food_kids", "priority": 3, "topic": "fruit", "french": "L'orange", "english": "Orange", "pronunciation": "loh-RAHNZH", "image": "\U0001F34A"},
    {"category": "food_kids", "priority": 3, "topic": "fruit", "french": "La fraise", "english": "Strawberry", "pronunciation": "lah FREHZ", "image": "\U0001F353"},
    {"category": "food_kids", "priority": 3, "topic": "fruit", "french": "Le raisin", "english": "Grape", "pronunciation": "luh reh-ZAHN", "image": "\U0001F347"},
    {"category": "food_kids", "priority": 3, "topic": "vegetables", "french": "La carotte", "english": "Carrot", "pronunciation": "lah kah-RUHT", "image": "\U0001F955"},
    {"category": "food_kids", "priority": 3, "topic": "vegetables", "french": "La tomate", "english": "Tomato", "pronunciation": "lah toh-MAHT", "image": "\U0001F345"},
    {"category": "food_kids", "priority": 3, "topic": "vegetables", "french": "Les petits pois", "english": "Peas", "pronunciation": "lay puh-TEE PWAH", "image": "\U0001FAD1"},
    {"category": "food_kids", "priority": 3, "topic": "drinks", "french": "Le jus", "english": "Juice", "pronunciation": "luh ZHOO", "image": "\U0001F9C3"},
    {"category": "food_kids", "priority": 3, "topic": "drinks", "french": "Le jus d'orange", "english": "Orange juice", "pronunciation": "luh zhoo doh-RAHNZH", "image": "\U0001F34A"},

    # =========================================================================
    # PRIORITY 4 - Helpful (More foods & phrases)
    # =========================================================================
    {"category": "food_kids", "priority": 4, "topic": "basics", "french": "L'oeuf", "english": "Egg", "pronunciation": "LUHF", "image": "\U0001F95A"},
    {"category": "food_kids", "priority": 4, "topic": "basics", "french": "Le beurre", "english": "Butter", "pronunciation": "luh BUHR", "image": "\U0001F9C8"},
    {"category": "food_kids", "priority": 4, "topic": "treats", "french": "Le chocolat", "english": "Chocolate", "pronunciation": "luh shoh-koh-LAH", "image": "\U0001F36B"},
    {"category": "food_kids", "priority": 4, "topic": "treats", "french": "Les bonbons", "english": "Sweets/Candy", "pronunciation": "lay bohn-BOHN", "image": "\U0001F36C"},
    {"category": "food_kids", "priority": 4, "topic": "treats", "french": "Le biscuit", "english": "Biscuit/Cookie", "pronunciation": "luh bees-KWEE", "image": "\U0001F36A"},
    {"category": "food_kids", "priority": 4, "topic": "meals", "french": "La soupe", "english": "Soup", "pronunciation": "lah SOOP", "image": "\U0001F963"},
    {"category": "food_kids", "priority": 4, "topic": "meals", "french": "Le sandwich", "english": "Sandwich", "pronunciation": "luh sahnd-WEESH", "image": "\U0001F96A"},
    {"category": "food_kids", "priority": 4, "topic": "phrases", "french": "C'est bon!", "english": "It's yummy!", "pronunciation": "seh BOHN"},

    # =========================================================================
    # PRIORITY 5 - Extra (Fun food phrases)
    # =========================================================================
    {"category": "food_kids", "priority": 5, "topic": "phrases", "french": "J'aime les pommes", "english": "I like apples", "pronunciation": "zhehm lay PUHM"},
    {"category": "food_kids", "priority": 5, "topic": "phrases", "french": "Je n'aime pas", "english": "I don't like", "pronunciation": "zhuh nehm PAH"},
    {"category": "food_kids", "priority": 5, "topic": "phrases", "french": "C'est délicieux!", "english": "It's delicious!", "pronunciation": "seh day-lee-SYUH"},
    {"category": "food_kids", "priority": 5, "topic": "phrases", "french": "Encore, s'il te plaît", "english": "More, please", "pronunciation": "ahn-KOHR seel tuh PLEH"},
    {"category": "food_kids", "priority": 5, "topic": "phrases", "french": "J'ai fini", "english": "I'm finished", "pronunciation": "zhay fee-NEE"},
    {"category": "food_kids", "priority": 5, "topic": "phrases", "french": "Je veux manger", "english": "I want to eat", "pronunciation": "zhuh vuh mahn-ZHAY"},
    {"category": "food_kids", "priority": 5, "topic": "phrases", "french": "Je veux boire", "english": "I want to drink", "pronunciation": "zhuh vuh BWAHR"},
    {"category": "food_kids", "priority": 5, "topic": "fruit", "french": "La pastèque", "english": "Watermelon", "pronunciation": "lah pahs-TEK", "image": "\U0001F349"},
]


# =============================================================================
# SENTENCE FRAMES VOCABULARY (Common structures)
# =============================================================================

SENTENCE_FRAMES_VOCABULARY = [
    # =========================================================================
    # PRIORITY 1 - Essential (Most useful sentence starters)
    # =========================================================================
    {"category": "sentence_frames", "priority": 1, "topic": "wanting", "french": "Je voudrais...", "english": "I would like...", "pronunciation": "zhuh voo-DREH"},
    {"category": "sentence_frames", "priority": 1, "topic": "wanting", "french": "Je veux...", "english": "I want...", "pronunciation": "zhuh VUH"},
    {"category": "sentence_frames", "priority": 1, "topic": "questions", "french": "Où est...?", "english": "Where is...?", "pronunciation": "oo EH"},
    {"category": "sentence_frames", "priority": 1, "topic": "questions", "french": "Est-ce que vous avez...?", "english": "Do you have...?", "pronunciation": "ess kuh vooz ah-VAY"},
    {"category": "sentence_frames", "priority": 1, "topic": "being", "french": "Je suis...", "english": "I am...", "pronunciation": "zhuh SWEE"},
    {"category": "sentence_frames", "priority": 1, "topic": "ability", "french": "Je peux...?", "english": "Can I...?", "pronunciation": "zhuh PUH"},
    {"category": "sentence_frames", "priority": 1, "topic": "needing", "french": "J'ai besoin de...", "english": "I need...", "pronunciation": "zhay buh-ZWAHN duh"},

    # =========================================================================
    # PRIORITY 2 - Very Common (Questions & polite requests)
    # =========================================================================
    {"category": "sentence_frames", "priority": 2, "topic": "questions", "french": "Est-ce que tu...?", "english": "Do you...? (informal)", "pronunciation": "ess kuh TOO"},
    {"category": "sentence_frames", "priority": 2, "topic": "questions", "french": "Est-ce que c'est...?", "english": "Is it...?", "pronunciation": "ess kuh SEH"},
    {"category": "sentence_frames", "priority": 2, "topic": "questions", "french": "Comment dit-on...?", "english": "How do you say...?", "pronunciation": "koh-MAHN dee TOHN"},
    {"category": "sentence_frames", "priority": 2, "topic": "questions", "french": "Qu'est-ce que c'est?", "english": "What is this?", "pronunciation": "kess kuh SEH"},
    {"category": "sentence_frames", "priority": 2, "topic": "questions", "french": "Il y a...?", "english": "Is there...?", "pronunciation": "eel ee AH"},
    {"category": "sentence_frames", "priority": 2, "topic": "having", "french": "J'ai...", "english": "I have...", "pronunciation": "ZHAY"},
    {"category": "sentence_frames", "priority": 2, "topic": "having", "french": "Je n'ai pas de...", "english": "I don't have...", "pronunciation": "zhuh nay PAH duh"},

    # =========================================================================
    # PRIORITY 3 - Common (Opinions & preferences)
    # =========================================================================
    {"category": "sentence_frames", "priority": 3, "topic": "opinions", "french": "Je pense que...", "english": "I think that...", "pronunciation": "zhuh PAHNS kuh"},
    {"category": "sentence_frames", "priority": 3, "topic": "opinions", "french": "Je crois que...", "english": "I believe that...", "pronunciation": "zhuh KRWAH kuh"},
    {"category": "sentence_frames", "priority": 3, "topic": "preferences", "french": "J'aime...", "english": "I like...", "pronunciation": "ZHEHM"},
    {"category": "sentence_frames", "priority": 3, "topic": "preferences", "french": "Je n'aime pas...", "english": "I don't like...", "pronunciation": "zhuh nehm PAH"},
    {"category": "sentence_frames", "priority": 3, "topic": "preferences", "french": "Je préfère...", "english": "I prefer...", "pronunciation": "zhuh pray-FEHR"},
    {"category": "sentence_frames", "priority": 3, "topic": "questions", "french": "Tu veux...?", "english": "Do you want...? (informal)", "pronunciation": "too VUH"},
    {"category": "sentence_frames", "priority": 3, "topic": "questions", "french": "Vous voulez...?", "english": "Do you want...? (formal)", "pronunciation": "voo voo-LAY"},
    {"category": "sentence_frames", "priority": 3, "topic": "actions", "french": "Je vais...", "english": "I'm going to...", "pronunciation": "zhuh VAY"},

    # =========================================================================
    # PRIORITY 4 - Helpful (Polite requests & explanations)
    # =========================================================================
    {"category": "sentence_frames", "priority": 4, "topic": "requests", "french": "Pourriez-vous...?", "english": "Could you...? (formal)", "pronunciation": "poo-ryay VOO"},
    {"category": "sentence_frames", "priority": 4, "topic": "requests", "french": "Pourrais-tu...?", "english": "Could you...? (informal)", "pronunciation": "poo-reh TOO"},
    {"category": "sentence_frames", "priority": 4, "topic": "requests", "french": "Est-ce que je pourrais...?", "english": "Could I...?", "pronunciation": "ess kuh zhuh poo-REH"},
    {"category": "sentence_frames", "priority": 4, "topic": "offers", "french": "Voulez-vous...?", "english": "Would you like...? (formal)", "pronunciation": "voo-lay VOO"},
    {"category": "sentence_frames", "priority": 4, "topic": "offers", "french": "Tu voudrais...?", "english": "Would you like...? (informal)", "pronunciation": "too voo-DREH"},
    {"category": "sentence_frames", "priority": 4, "topic": "explaining", "french": "C'est parce que...", "english": "It's because...", "pronunciation": "seh pahrs KUH"},
    {"category": "sentence_frames", "priority": 4, "topic": "explaining", "french": "Je cherche...", "english": "I'm looking for...", "pronunciation": "zhuh SHEHRSH"},
    {"category": "sentence_frames", "priority": 4, "topic": "actions", "french": "Je viens de...", "english": "I just (did)...", "pronunciation": "zhuh VYEHN duh"},

    # =========================================================================
    # PRIORITY 5 - Extra (Advanced structures)
    # =========================================================================
    {"category": "sentence_frames", "priority": 5, "topic": "conditions", "french": "Si j'avais...", "english": "If I had...", "pronunciation": "see zhah-VEH"},
    {"category": "sentence_frames", "priority": 5, "topic": "conditions", "french": "Quand je serai...", "english": "When I will be...", "pronunciation": "kahn zhuh suh-REH"},
    {"category": "sentence_frames", "priority": 5, "topic": "opinions", "french": "Il me semble que...", "english": "It seems to me that...", "pronunciation": "eel muh SAHM-bluh kuh"},
    {"category": "sentence_frames", "priority": 5, "topic": "opinions", "french": "À mon avis...", "english": "In my opinion...", "pronunciation": "ah mohn ah-VEE"},
    {"category": "sentence_frames", "priority": 5, "topic": "comparing", "french": "C'est plus... que...", "english": "It's more... than...", "pronunciation": "seh PLOO ... kuh"},
    {"category": "sentence_frames", "priority": 5, "topic": "comparing", "french": "C'est moins... que...", "english": "It's less... than...", "pronunciation": "seh MWAHN ... kuh"},
    {"category": "sentence_frames", "priority": 5, "topic": "wondering", "french": "Je me demande si...", "english": "I wonder if...", "pronunciation": "zhuh muh duh-MAHND see"},
    {"category": "sentence_frames", "priority": 5, "topic": "suggesting", "french": "On pourrait...", "english": "We could...", "pronunciation": "ohn poo-REH"},
]


# =============================================================================
# PODCAST VOCABULARY (Coffee Break French)
# =============================================================================

PODCAST_VOCABULARY = [
    {"category": "podcast", "priority": 1, "topic": "coffee_break_ep1", "french": "Oui", "english": "Yes", "pronunciation": "wee"},
    {"category": "podcast", "priority": 1, "topic": "coffee_break_ep1", "french": "Non", "english": "No", "pronunciation": "nohn"},
    {"category": "podcast", "priority": 1, "topic": "coffee_break_ep1", "french": "S'il vous plaît", "english": "Please (formal)", "pronunciation": "seel voo PLEH"},
    {"category": "podcast", "priority": 1, "topic": "coffee_break_ep1", "french": "Très bien", "english": "Very well / Very good", "pronunciation": "treh BYEHN"},
    {"category": "podcast", "priority": 1, "topic": "coffee_break_ep1", "french": "Merci", "english": "Thank you", "pronunciation": "mehr-SEE"},
    {"category": "podcast", "priority": 1, "topic": "coffee_break_ep1", "french": "Et toi?", "english": "And you? (informal)", "pronunciation": "ay TWAH"},
    {"category": "podcast", "priority": 1, "topic": "coffee_break_ep1", "french": "Ça ne va pas", "english": "I'm not well", "pronunciation": "sah nuh vah PAH"},
    {"category": "podcast", "priority": 1, "topic": "coffee_break_ep1", "french": "Excellent", "english": "Excellent", "pronunciation": "ehk-seh-LAHN"},
    {"category": "podcast", "priority": 1, "topic": "coffee_break_ep1", "french": "Je suis fatigué", "english": "I am tired", "pronunciation": "zhuh swee fah-tee-GAY"},
    {"category": "podcast", "priority": 1, "topic": "coffee_break_ep1", "french": "Je suis en forme", "english": "I am fit / in good shape", "pronunciation": "zhuh swee ahn FOHRM"},
]


# Combine all vocabulary
DEFAULT_VOCABULARY = GENERAL_VOCABULARY + ANIMALS_VOCABULARY + COLOURS_VOCABULARY + BODY_PARTS_VOCABULARY + FOOD_VOCABULARY + SENTENCE_FRAMES_VOCABULARY + PODCAST_VOCABULARY


# =============================================================================
# FUNCTIONS
# =============================================================================

def add_card(category: str, topic: str, french: str, english: str,
             pronunciation: str = None, priority: int = 3, image: str = None) -> int:
    """Add a new vocabulary card."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO cards (category, topic, french, english, pronunciation, priority, image)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (category, topic, french, english, pronunciation, priority, image))

    card_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return card_id


def add_cards_bulk(cards: list) -> int:
    """Add multiple cards at once."""
    conn = get_connection()
    cursor = conn.cursor()

    for card in cards:
        if 'category' not in card:
            card['category'] = 'general'
        if 'priority' not in card:
            card['priority'] = 3
        if 'image' not in card:
            card['image'] = None

    cursor.executemany("""
        INSERT INTO cards (category, topic, french, english, pronunciation, priority, image)
        VALUES (:category, :topic, :french, :english, :pronunciation, :priority, :image)
    """, cards)

    count = cursor.rowcount
    conn.commit()
    conn.close()

    return count


def get_card(card_id: int) -> dict:
    """Get a single card by ID."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cards WHERE id = ?", (card_id,))
    row = cursor.fetchone()
    conn.close()

    return dict(row) if row else None


def get_cards(category: str = None, topic: str = None, priority: int = None) -> list:
    """Get all cards, optionally filtered."""
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM cards WHERE 1=1"
    params = []

    if category:
        query += " AND category = ?"
        params.append(category)

    if topic:
        query += " AND topic = ?"
        params.append(topic)

    if priority:
        query += " AND priority = ?"
        params.append(priority)

    query += " ORDER BY category, priority, id"
    cursor.execute(query, params)

    cards = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return cards


def get_categories() -> list:
    """Get list of all categories with card counts."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, COUNT(*) as count
        FROM cards
        GROUP BY category
        ORDER BY category
    """)

    categories = [{'category': row['category'], 'count': row['count']} for row in cursor.fetchall()]
    conn.close()

    return categories


def get_topics(category: str = None) -> list:
    """Get list of all topics with card counts."""
    conn = get_connection()
    cursor = conn.cursor()

    if category:
        cursor.execute("""
            SELECT topic, COUNT(*) as count
            FROM cards
            WHERE category = ?
            GROUP BY topic
            ORDER BY topic
        """, (category,))
    else:
        cursor.execute("""
            SELECT topic, COUNT(*) as count
            FROM cards
            GROUP BY topic
            ORDER BY topic
        """)

    topics = [{'topic': row['topic'], 'count': row['count']} for row in cursor.fetchall()]
    conn.close()

    return topics


def get_priorities(category: str = None) -> list:
    """Get card counts by priority level."""
    conn = get_connection()
    cursor = conn.cursor()

    if category:
        cursor.execute("""
            SELECT priority, COUNT(*) as count
            FROM cards
            WHERE category = ?
            GROUP BY priority
            ORDER BY priority
        """, (category,))
    else:
        cursor.execute("""
            SELECT priority, COUNT(*) as count
            FROM cards
            GROUP BY priority
            ORDER BY priority
        """)

    priorities = [{'priority': row['priority'], 'count': row['count']} for row in cursor.fetchall()]
    conn.close()

    return priorities


def update_card(card_id: int, **fields) -> bool:
    """Update a card's fields."""
    allowed = {'french', 'english', 'pronunciation', 'topic', 'priority', 'category', 'image'}
    updates = {k: v for k, v in fields.items() if k in allowed}

    if not updates:
        return False

    conn = get_connection()
    cursor = conn.cursor()

    set_clause = ', '.join(f'{k} = ?' for k in updates.keys())
    values = list(updates.values()) + [card_id]

    cursor.execute(f"UPDATE cards SET {set_clause} WHERE id = ?", values)
    updated = cursor.rowcount > 0

    conn.commit()
    conn.close()

    return updated


def delete_card(card_id: int) -> bool:
    """Delete a card and its progress data."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM review_history WHERE card_id = ?", (card_id,))
    cursor.execute("DELETE FROM progress WHERE card_id = ?", (card_id,))
    cursor.execute("DELETE FROM cards WHERE id = ?", (card_id,))

    deleted = cursor.rowcount > 0
    conn.commit()
    conn.close()

    return deleted


def search_cards(query: str, category: str = None) -> list:
    """Search cards by French or English text."""
    conn = get_connection()
    cursor = conn.cursor()

    search = f'%{query}%'

    if category:
        cursor.execute("""
            SELECT * FROM cards
            WHERE (french LIKE ? OR english LIKE ?) AND category = ?
            ORDER BY priority, id
        """, (search, search, category))
    else:
        cursor.execute("""
            SELECT * FROM cards
            WHERE french LIKE ? OR english LIKE ?
            ORDER BY category, priority, id
        """, (search, search))

    cards = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return cards


def load_default_vocabulary() -> int:
    """Load the default vocabulary into the database."""
    return add_cards_bulk(DEFAULT_VOCABULARY)


def reset_vocabulary():
    """Reset vocabulary to defaults (clears all progress too)."""
    from database import reset_db
    reset_db()
    from users import setup_default_users
    setup_default_users()
    load_default_vocabulary()


def card_count(category: str = None) -> int:
    """Get total number of cards."""
    conn = get_connection()
    cursor = conn.cursor()

    if category:
        cursor.execute("SELECT COUNT(*) FROM cards WHERE category = ?", (category,))
    else:
        cursor.execute("SELECT COUNT(*) FROM cards")

    count = cursor.fetchone()[0]
    conn.close()
    return count


# Auto-load default vocabulary if database is empty
if card_count() == 0:
    load_default_vocabulary()
