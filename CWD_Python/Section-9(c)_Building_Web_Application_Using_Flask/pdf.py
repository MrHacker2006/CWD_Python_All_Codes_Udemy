from fpdf import FPDF

# List of all important random functions
random_functions = [
    {
        "Function": "random.randint(a, b)",
        "Description": "Generates a random integer N such that a <= N <= b.",
        "UseCase": "🎲 Dice games, 🔢 OTP generation, 🎫 Random ticket number"
    },
    {
        "Function": "random.random()",
        "Description": "Returns a random float number between 0.0 and 1.0.",
        "UseCase": "🎯 Probability, 🎮 Game logic randomness"
    },
    {
        "Function": "random.uniform(a, b)",
        "Description": "Returns a random float N such that a <= N <= b.",
        "UseCase": "📊 Simulations, 📈 Price fluctuations"
    },
    {
        "Function": "random.choice(seq)",
        "Description": "Returns a randomly selected element from a non-empty sequence.",
        "UseCase": "🎮 Random item drop, 🤖 Chatbot responses"
    },
    {
        "Function": "random.choices(population, weights=None, k=1)",
        "Description": "Returns a list with k elements with replacement.",
        "UseCase": "🎁 Loot boxes, 🧪 Sampling with probability"
    },
    {
        "Function": "random.shuffle(seq)",
        "Description": "Shuffles the sequence in place.",
        "UseCase": "🃏 Deck shuffling, 🎧 Playlist shuffle"
    },
    {
        "Function": "random.sample(population, k)",
        "Description": "Returns k unique elements from a population (no replacement).",
        "UseCase": "🎟️ Raffle draws, ✅ Sampling without replacement"
    },
    {
        "Function": "random.seed(a=None)",
        "Description": "Seeds the random generator (for reproducibility).",
        "UseCase": "🧪 Testing, 📁 Consistent results"
    },
    {
        "Function": "random.randrange(start, stop[, step])",
        "Description": "Returns a randomly selected element from range(start, stop, step).",
        "UseCase": "🔁 Index picking, 🔢 Random skipping loops"
    },
    {
        "Function": "random.betavariate(alpha, beta)",
        "Description": "Returns a float sampled from a Beta distribution.",
        "UseCase": "📉 Bayesian statistics, 📈 Machine learning models"
    },
    {
        "Function": "random.gauss(mu, sigma)",
        "Description": "Returns a float from Gaussian distribution with mean mu and standard deviation sigma.",
        "UseCase": "📈 Stock price sim, 🎯 ML data generation"
    },
    {
        "Function": "random.expovariate(lambd)",
        "Description": "Returns a float from exponential distribution with rate λ.",
        "UseCase": "📞 Call arrival simulation, 🔧 Queuing models"
    },
    {
        "Function": "random.triangular(low, high, mode)",
        "Description": "Returns a random float in a triangular distribution.",
        "UseCase": "📦 Delivery time estimation, 🎮 Game event timing"
    },
    {
        "Function": "random.normalvariate(mu, sigma)",
        "Description": "Returns a float from normal distribution (Gaussian).",
        "UseCase": "📊 Stats modeling, 🧠 Neural inputs noise"
    }
]

# Define PDF class
class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(30, 30, 120)
        self.cell(0, 10, "🚀 Python 'random' Library - Full Function Table", ln=True, align="C")
        self.ln(5)

    def table_header(self):
        self.set_font("Helvetica", "B", 12)
        self.set_fill_color(200, 220, 255)
        self.cell(65, 10, "Function", border=1, align="C", fill=True)
        self.cell(75, 10, "Description", border=1, align="C", fill=True)
        self.cell(50, 10, "Use-Case", border=1, ln=True, align="C", fill=True)

    def table_body(self, data):
        self.set_font("Helvetica", "", 11)
        for func in data:
            self.set_fill_color(245, 245, 245)
            self.cell(65, 20, func["Function"], border=1)
            self.multi_cell(75, 10, func["Description"], border=1, align="L")
            x = self.get_x()
            y = self.get_y()
            self.set_xy(x + 140, y - 20)
            self.multi_cell(50, 10, func["UseCase"], border=1, align="L")
            self.set_xy(10, y)

# Create and generate PDF
pdf = PDF()
pdf.add_page()
pdf.table_header()
pdf.table_body(random_functions)

# Save file
pdf.output("Full_Random_Library_Functions_Table.pdf")
print("✅ PDF saved as 'Full_Random_Library_Functions_Table.pdf'")
