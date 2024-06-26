import pandas as pd

# Create a DataFrame from the markdown table
data = {
    "Question": [
        "What is Ayurveda?",
        "What are the beliefs in Ayurveda?",
        "Why should one use the teachings in Ayurveda?"
    ],
    "LLM + KG": [
        "Ayurveda is a traditional Indian system of medicine. It translates to \"knowledge of life\" and emphasizes a holistic approach to health, considering the mind, body, and spirit interconnected. Ayurveda uses natural remedies like herbs, diet, and lifestyle changes to balance the body's energies and promote well-being.",
        "Ayurveda is based on the belief that health and wellness depend on a delicate balance between the mind, body, and spirit. It emphasizes the idea that everything in the universe, including humans, is composed of five elements: earth, water, fire, air, and ether. These elements combine in the body to form three life forces or energies called doshas: Vata, Pitta, and Kapha. Each dosha has unique characteristics and maintaining their balance is considered crucial for good health. Imbalances are believed to lead to disease.",
        "People turn to Ayurveda for its holistic approach to well-being. Instead of just addressing symptoms, Ayurveda aims to identify and address the root cause of imbalances within the individual. It emphasizes disease prevention, stress reduction, and living in harmony with nature. Many find the focus on natural remedies and personalized lifestyle changes appealing for maintaining good health."
    ],
    "LLM": [
        "Ayurveda is an ancient Indian system of medicine that aims to maintain health and well-being by balancing the body, mind, and spirit. It emphasizes personalized treatments, including diet, herbs, yoga, and meditation, based on an individual's unique constitution and life energies (doshas).",
        "Ayurveda is a holistic healing system that originated in India over 5,000 years ago. It is based on the belief that health and wellness depend on a delicate balance between the mind, body, and spirit.\n\nKey beliefs include:\n\n* Universe is made up of five elements: Earth, water, fire, air, and ether.\n* These elements combine in the body to form three doshas: Vata (air and ether), Pitta (fire and water), and Kapha (earth and water).\n* Each person has a unique balance of these doshas, which determines their physical and mental characteristics.\n* Illness arises from an imbalance in the doshas.\n* Balance is restored through diet, lifestyle changes, herbs, massage, and other therapies.\n\nAyurveda emphasizes preventative care and maintaining balance to achieve optimal health and well-being.",
        "Ayurveda offers a holistic approach to health, focusing on balancing mind, body, and spirit for overall well-being. It emphasizes preventative measures and personalized treatments using natural remedies, promoting long-term health and vitality."
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
file_path = "Ayurveda_QA.xlsx"
df.to_excel(file_path, index=False)
