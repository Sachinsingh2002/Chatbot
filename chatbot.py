# Sachin Singh 
# 5th JUNE 2023
# 12:45 AM




from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    bot_response = process_input(user_input)
    return bot_response


def process_input(user_input):
    
    if user_input.lower() == 'hello':
        return "Hi there!"
    elif user_input.lower() == 'how are you?':
        return "I'm doing well, thank you!"
    elif user_input.lower() == 'bye':
        return "Goodbye!"
    elif user_input.lower() == 'how are you':
        return "I'm doing well, thank you!"
    elif user_input.lower() == 'hi':
        return "Hello, How can I help you"
    
    elif user_input.lower() == 'another joke':
        return "Two programmers are talking about their social life, and one says: The only date I get is the Java Update."
    elif user_input.lower() == 'jai shri ram':
        return "jai shree ram"
    elif user_input.lower() == 'jai shri ram':
        return "jai shri ram"
    elif user_input.lower() == 'whats the weather':
        return "Cloudy"
    elif user_input.lower() == 'translate hello to french':
        return "The translation of hello to French is bonjour."
    elif user_input.lower() == 'who is your favorite teacher':
        return "Sonia Rani mam"
    elif user_input.lower() == 'best prime minister':
        return "Narendra Damodardas Modi"
    elif user_input.lower() == 'prime minister of india':
        return "Narendra Damodardas Modi"
    elif user_input.lower() == 'who is the god father':
        return "krishna"
    
    elif user_input.lower() == 'president of the United States':
        return "Joe Biden"
    elif user_input.lower() == 'chancellor of Germany':
        return "Angela Merkel"
    elif user_input.lower() == 'prime minister of the United Kingdom':
        return "Boris Johnson"
    elif user_input.lower() == 'president of France':
        return "Emmanuel Macron"
    
    elif user_input.lower() == 'what is your name?':
        return "My name is Chatbot. Nice to meet you!"

    elif user_input.lower() == 'tell me a joke':
        return "Why don't scientists trust atoms? Because they make up everything!"

    elif user_input.lower() == 'who created you?':
        return "I was created by a team of developers at OpenAI."

    elif user_input.lower() == 'what is the meaning of life?':
        return "The meaning of life is subjective and can vary for each individual."

    elif user_input.lower() == 'do you have any hobbies?':
        return "As an AI, I don't have physical hobbies, but I enjoy learning and assisting users."

    elif  user_input.lower() == 'tell me a fun fact':
        return "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!"

    elif user_input.lower() == 'where are you from?':
        return "I am a virtual assistant, so I don't have a physical location. But I'm here to help you!"

    elif user_input.lower() == 'what is the capital of France?':
        return "The capital of France is Paris."
    
    #related to science

    elif user_input.lower() == 'can you help me with math problems?':
        return "Of course! I can assist you with various math problems. Just let me know what you need help with."

    elif user_input.lower() == 'what is your favorite movie?':
        return "As an AI, I don't have preferences or favorites, but I can recommend popular movies if you'd like."

    elif  user_input.lower() == 'what is the speed of light?':
        return "The speed of light in a vacuum is approximately 299,792,458 meters per second."

    elif user_input.lower() == 'what is the formula for calculating force?':
        return "The formula for calculating force is F = m * a, where F represents force, m represents mass, and a represents acceleration."

    elif user_input.lower() == 'what is the equation for Einsteins theory of relativity?':
        return "E = mc^2, where E represents energy, m represents mass, and c represents the speed of light."

    elif user_input.lower() == 'what is the structure of an atom?':
        return "Atoms consist of a nucleus made up of protons and neutrons, surrounded by electrons in energy levels or shells."

    elif user_input.lower() == 'what is the law of conservation of energy?':
        return "The law of conservation of energy states that energy cannot be created or destroyed, only transferred or transformed from one form to another."

    elif user_input.lower() == 'what is the periodic table?':
        return "The periodic table is a tabular arrangement of chemical elements, organized based on their atomic number, electron configuration, and recurring chemical properties."

    elif user_input.lower() == 'what is the process of photosynthesis?':
        return "Photosynthesis is the process by which plants, algae, and some bacteria convert sunlight, carbon dioxide, and water into glucose and oxygen, using chlorophyll as a catalyst."

    elif user_input.lower() == 'what is the theory of evolution?':
        return "The theory of evolution, proposed by Charles Darwin, states that species change over time through the process of natural selection, where those with favorable traits are more likely to survive and reproduce."

    elif user_input.lower() == 'what is the concept of entropy?':
        return "Entropy is a measure of the disorder or randomness in a system. In thermodynamics, it is often associated with the second law, which states that the entropy of an isolated system tends to increase over time."

    elif user_input.lower() == 'what is the structure of DNA?':
        return "DNA (deoxyribonucleic acid) has a double helix structure consisting of two strands made up of nucleotides. The four nucleotides are adenine (A), thymine (T), cytosine (C), and guanine (G), which form complementary base pairs."

    #related to space

    elif user_input.lower() == 'what is a supernova?':
        return "A supernova is a powerful and luminous explosion that occurs at the end of a star's life, releasing an enormous amount of energy and producing elements heavier than iron."

    elif user_input.lower() == 'what is the Big Bang theory?':
        return "The Big Bang theory is the prevailing cosmological model that explains the origin and evolution of the universe. It suggests that the universe began as a hot, dense state and has been expanding ever since."

    elif user_input.lower() == 'what is a galaxy?':
        return "A galaxy is a vast collection of stars, gas, dust, and other celestial objects held together by gravity. The Milky Way is an example of a galaxy."

    elif user_input.lower() == 'what is a nebula?':
        return "A nebula is a cloud of gas and dust in space. It is often a site of star formation and can exhibit beautiful and intricate structures."

    elif user_input.lower() == 'what is an exoplanet?':
        return "An exoplanet is a planet that orbits a star outside of our solar system. They provide valuable insights into planetary formation and the potential for extraterrestrial life."

    elif user_input.lower() == 'what is the Mars Rover?':
        return "The Mars Rover is a robotic vehicle sent by NASA to explore the surface of Mars, gathering data and searching for signs of past or present microbial life."

    elif user_input.lower() == 'what is a lunar eclipse?':
        return "A lunar eclipse occurs when the Earth passes between the Sun and the Moon, casting a shadow on the Moon and causing it to appear dark or reddish."

    elif user_input.lower() == 'what is the International Space Station (ISS)?':
        return "The International Space Station is a habitable space station that serves as a laboratory for scientific research and international cooperation in space exploration."

    #related to technology

    elif user_input.lower() == 'what is artificial intelligence?':
        return "Artificial intelligence (AI) is a field of computer science that focuses on creating intelligent machines capable of performing tasks that typically require human intelligence."

    elif user_input.lower() == 'what is machine learning?':
        return "Machine learning is a subset of AI that involves training computer systems to learn from data and make predictions or take actions without being explicitly programmed."

    elif user_input.lower() == 'what is blockchain?':
        return "Blockchain is a decentralized and distributed digital ledger technology that enables secure and transparent transactions across multiple participants."
    elif user_input.lower() == 'what is virtual reality?':
        return "Virtual reality (VR) is a technology that uses computer-generated environments to simulate a realistic sensory experience, often through a head-mounted display and motion tracking."

    elif user_input.lower() == 'what is the Internet of Things (IoT)?':
        return "The Internet of Things refers to the network of physical devices, vehicles, appliances, and other objects embedded with sensors, software, and connectivity to exchange data and interact with each other."

    elif user_input.lower() == 'what is cybersecurity?':
        return "Cybersecurity is the practice of protecting computer systems, networks, and data from unauthorized access, use, disclosure, disruption, modification, or destruction, ensuring confidentiality, integrity, and availability."

    elif user_input.lower() == 'what is cloud computing?':
        return "Cloud computing is the delivery of on-demand computing resources over the internet, allowing users to access and use computational power, storage, and applications without needing to have physical infrastructure."

    elif user_input.lower() == 'what is augmented reality?':
        return "Augmented reality (AR) is a technology that overlays digital information, such as virtual objects or real-time data, onto the real-world environment, enhancing the user's perception and interaction."

    elif user_input.lower() == 'what is data science?':
        return "Data science is an interdisciplinary field that involves extracting knowledge and insights from structured and unstructured data using scientific methods, processes, algorithms, and systems."

    elif user_input.lower() == 'what is 3D printing?':
        return "3D printing, also known as additive manufacturing, is a process of creating three-dimensional objects by layering or depositing materials based on a digital model."

    #related to  general knowledge

    elif user_input.lower() == 'what is the capital of Australia?':
        return "The capital of Australia is Canberra."

    elif user_input.lower() == 'who painted the Mona Lisa?':
        return "The Mona Lisa was painted by Leonardo da Vinci."

    elif user_input.lower() == 'what is the largest ocean in the world?':
        return "The largest ocean in the world is the Pacific Ocean."

    elif user_input.lower() == 'who wrote the play Romeo and Juliet?':
        return "The play Romeo and Juliet was written by William Shakespeare."

    elif user_input.lower() == 'what is the currency of Japan?':
        return "The currency of Japan is the Japanese yen."

    elif user_input.lower() == 'what is the tallest mountain in the world?':
        return "The tallest mountain in the world is Mount Everest."

    elif user_input.lower() == 'who discovered gravity?':
        return "Gravity was described by Sir Isaac Newton."

    elif user_input.lower() == 'what is the national animal of Canada?':
        return "The national animal of Canada is the beaver."

    elif user_input.lower() == 'who invented the telephone?':
        return "The telephone was invented by Alexander Graham Bell."

    elif user_input.lower() == 'what is the largest planet in our solar system?':
        return "The largest planet in our solar system is Jupiter."
    
    #related to daily life

    elif user_input.lower() == 'what is the recipe for chocolate chip cookies?':
        return "Here's a simple recipe for chocolate chip cookies: Combine butter, sugar, eggs, vanilla extract, flour, baking soda, salt, and chocolate chips. Mix well, scoop onto a baking sheet, and bake at 350°F (175°C) for about 10-12 minutes."

    elif user_input.lower() == 'how do I tie a tie?':
        return "To tie a tie, start with the wide end over the narrow end. Cross the wide end over the narrow end, bring it up and through the loop, then down through the knot. Tighten and adjust until it's symmetrical."

    elif user_input.lower() == 'what is the best way to organize my schedule?':
        return "One effective way to organize your schedule is to use a digital calendar or planner app. Set specific time blocks for tasks, prioritize important activities, and set reminders to help you stay on track."

    elif user_input.lower() == 'how can I improve my productivity?':
        return "To improve productivity, consider using time management techniques like the Pomodoro Technique, breaking tasks into smaller, manageable steps, eliminating distractions, and maintaining a balanced work-life routine."

    elif user_input.lower() == 'what are some tips for staying healthy?':
        return "To stay healthy, focus on maintaining a balanced diet, engaging in regular exercise, getting enough sleep, managing stress, staying hydrated, and practicing good hygiene."

    elif user_input.lower() == 'how do I change a flat tire?':
        return "To change a flat tire, park in a safe location, use a jack to lift the vehicle, remove the lug nuts, replace the flat tire with the spare, tighten the lug nuts, and lower the vehicle."

    elif user_input.lower() == 'what is a good way to manage finances?':
        return "To manage finances effectively, create a budget, track expenses, prioritize saving and investing, avoid unnecessary debt, and seek professional advice if needed."

    elif user_input.lower() == 'how can I improve my communication skills?':
        return "To improve communication skills, practice active listening, express ideas clearly and concisely, seek feedback, engage in conversations, and develop empathy and understanding."

    elif user_input.lower() == 'what are some tips for effective studying?':
        return "To study effectively, create a conducive environment, break study sessions into manageable chunks, use active learning techniques like summarizing and self-quizzing, and take regular breaks to maintain focus."

    elif user_input.lower() == 'what is a good way to reduce stress?':
        return "To reduce stress, try relaxation techniques like deep breathing and meditation, engage in physical activity, prioritize self-care, maintain a support network, and seek professional help if needed."

    #related to normal conversation

    elif user_input.lower() == 'whats your favorite movie?':
        return "As an AI, I don't have personal preferences, but some popular movies include The Shawshank Redemption, The Godfather, and Pulp Fiction."

    elif user_input.lower() == 'whats your favorite music genre?':
        return "As an AI, I don't have personal preferences, but I can appreciate various music genres like pop, rock, classical, and hip-hop."

    elif user_input.lower() == 'what do you like to do for fun?':
        return "I enjoy assisting users, answering questions, and providing helpful information. I'm always here to have a conversation!"

    elif user_input.lower() == 'what are your hobbies?':
        return "As an AI, I don't have hobbies in the same way humans do. However, I enjoy learning, analyzing data, and helping people."

    elif user_input.lower() == 'whats your favorite book?':
        return "As an AI, I don't have personal favorites, but some popular books include To Kill a Mockingbird, 1984, and Pride and Prejudice."

    elif user_input.lower() == 'do you have any pets?':
        return "As an AI, I don't have physical presence, so I don't have pets. But I can provide information about different types of pets!"

    elif user_input.lower() == 'tell me a joke!':
        return "Sure, here's a joke: Why don't scientists trust atoms? Because they make up everything!"

    elif user_input.lower() == 'whats your favorite food?':
        return "As an AI, I don't have personal preferences for food. However, I can help you find recipes or recommend popular dishes!"
    elif user_input.lower() == 'what are your plans for the weekend?':
        return "As an AI, I don't have plans for the weekend. But I'll be here, ready to assist you with any questions or tasks you have!"

    #related to sports

    elif user_input.lower() == 'who won the last Super Bowl?':
        return "The last Super Bowl was won by [insert winning team]."

    elif user_input.lower() == 'who is the current NBA champion?':
        return "The current NBA champion is [insert team name]."

    elif user_input.lower() == 'who holds the record for the most goals scored in soccer?':
        return "The record for the most goals scored in soccer is held by [insert player's name]."
    elif user_input.lower() == 'what is the most-watched sporting event in the world?':
        return "The most-watched sporting event in the world is the [insert event name], with billions of viewers tuning in."

    elif user_input.lower() == 'who is the current Formula 1 world champion?':
        return "The current Formula 1 world champion is [insert driver's name]."

    elif user_input.lower() == 'what is the oldest tennis tournament in the world?':
        return "The oldest tennis tournament in the world is [insert tournament name], dating back to [insert year]."

    elif user_input.lower() == 'who is the most decorated Olympian of all time?':
        return "The most decorated Olympian of all time is [insert athlete's name], with [insert number] medals."

    elif user_input.lower() == 'who won the last FIFA World Cup?':
        return "The last FIFA World Cup was won by [insert winning team]."

    elif user_input.lower() == 'who holds the record for the most home runs in baseball?':
        return "The record for the most home runs in baseball is held by [insert player's name]."

    elif user_input.lower() == 'who is considered the greatest basketball player of all time?':
        return "Many consider [insert player's name] to be the greatest basketball player of all time."

    #related to cricket

    elif user_input.lower() == 'who is the current captain of the Indian cricket team?':
        return "The current captain of the Indian cricket team is Rohit Sharma."

    elif user_input.lower() == 'who holds the record for the highest individual score in Test cricket?':
        return "The record for the highest individual score in Test cricket is held by BC Lara with 400 Runs."

    elif user_input.lower() == 'who won the last ICC Cricket World Cup?':
        return "The last ICC Cricket World Cup was won by England."

    elif user_input.lower() == 'who is the leading run-scorer in One Day Internationals (ODIs)?':
        return "The leading run-scorer in ODIs is Sachin TEndulkar with 18426 Runs."

    elif user_input.lower() == 'who is the leading wicket-taker in Test cricket?':
        return "The leading wicket-taker in Test cricket is M Muralidaran with 800 Wickets."

    elif user_input.lower() == 'who won the last Indian Premier League (IPL)?':
        return "The last Indian Premier League (IPL) was won by Cheannai Super Kings."

    elif user_input.lower() == 'who is the fastest bowler in the history of cricket?':
        return "The title for the fastest bowler in the history of cricket is debated, but some notable names include Shoaib Akhtar."

    elif user_input.lower() == 'who is the highest run-scorer in Twenty20 Internationals (T20Is)?':
        return "The highest run-scorer in T20 Internationals is Virat Kohli with 4008 Runs."

    elif user_input.lower() == 'who is considered the greatest cricketer of all time?':
        return "There are many great cricketers, but some names often mentioned as the greatest include Sir donald Bradman."

    elif user_input.lower() == 'who won the last ICC Champions Trophy?':
        return "The last ICC Champions Trophy was won by PAkistan."

    #related to football

    elif user_input.lower() == 'who won the last FIFA World Cup?':
        return "The last FIFA World Cup was won by Argintina."

    elif user_input.lower() == 'who is the current Ballon d Or winner?':
        return "The current Ballon d'Or winner is Karim Benzema."

    elif user_input.lower() == 'who is the all-time leading goalscorer in international football?':
        return "The all-time leading goalscorer in international football is Cristiano Ronaldo with 122 Goals."

    elif user_input.lower() == 'who won the last UEFA Champions League?':
        return "The last UEFA Champions League was won by Real Madrid."

    elif user_input.lower() == 'who is the current top scorer in the English Premier League?':
        return "The current top scorer in the English Premier League is Erling Haaland with 36 Goals."

    elif user_input.lower() == 'who is the most successful club in the history of the UEFA Champions League?':
        return "The most successful club in the history of the UEFA Champions League is Real Madred with 14 Times."

    elif user_input.lower() == 'who won the last Copa America?':
        return "The last Copa America was won by Argrntina."

    elif user_input.lower() == 'who is the current FIFA World Cup Golden Boot holder?':
        return "The current FIFA World Cup Golden Boot holder is Kylian Mbappe with 5 Goals in Qatar."

    elif user_input.lower() == 'who is the most expensive football player in history?':
        return "The most expensive football player in history is Neymar."

    elif user_input.lower() == 'who is the current manager of Real Madred?':
        return "The current manager of [insert team name] is Carlo Ancelotti."
    
    #related to outer space


    elif user_input.lower() == 'what is the largest planet in our solar system?':
        return "The largest planet in our solar system is Jupiter."

    elif user_input.lower() == 'how far is the Moon from Earth?':
        return "The average distance between the Moon and Earth is about 384,400 kilometers (238,900 miles)."

    elif user_input.lower() == 'what is a black hole?':
        return "A black hole is a region in space with extremely strong gravitational forces that nothing, not even light, can escape from."

    elif user_input.lower() == 'what is the name of our galaxy?':
        return "Our galaxy is called the Milky Way."
    elif user_input.lower() == 'what is a supernova?':
        return "A supernova is a powerful and luminous explosion that occurs when a massive star reaches the end of its life."

    elif user_input.lower() == 'what is the Hubble Space Telescope?':
        return "The Hubble Space Telescope is a space-based observatory that has provided stunning images and valuable data about the universe."

    elif user_input.lower() == 'what is a nebula?':
        return "A nebula is a vast cloud of gas and dust in space, often illuminated by nearby stars or other energy sources."

    elif user_input.lower() == 'what is the name of the nearest star to Earth?':
        return "The nearest star to Earth, apart from the Sun, is Proxima Centauri."

    elif user_input.lower() == 'what is the purpose of a space probe?':
        return "Space probes are unmanned spacecraft sent to explore celestial bodies, gather data, and conduct scientific research."

    elif user_input.lower() == 'what is the concept of "space-time" in physics?':
        return "In physics, space-time is a four-dimensional framework that combines space and time into a single unified concept, as described by Einstein's theory of general relativity."

    #related to education

    elif user_input.lower() == 'what is the capital of France?':
        return "The capital of France is Paris."

    elif user_input.lower() == 'who is the author of the novel "Pride and Prejudice"?':
        return "The author of the novel 'Pride and Prejudice' is Jane Austen."

    elif user_input.lower() == 'what is the chemical symbol for gold?':
        return "The chemical symbol for gold is Au."

    elif user_input.lower() == 'what is the square root of 25?':
        return "The square root of 25 is 5."

    elif user_input.lower() == 'who discovered the theory of relativity?':
        return "The theory of relativity was discovered by Albert Einstein."

    elif user_input.lower() == 'what is the formula to calculate the area of a circle?':
        return "The formula to calculate the area of a circle is A = πr^2, where A is the area and r is the radius."

    elif user_input.lower() == 'who painted the Mona Lisa?':
        return "The Mona Lisa was painted by Leonardo da Vinci."

    elif user_input.lower() == 'what is the longest river in the world?':
        return "The longest river in the world is the Nile River."

    elif user_input.lower() == 'what is the formula to calculate the volume of a cylinder?':
        return "The formula to calculate the volume of a cylinder is V = πr^2h, where V is the volume, r is the radius, and h is the height."

    elif user_input.lower() == 'who wrote the play "Romeo and Juliet"?':
        return "The play 'Romeo and Juliet' was written by William Shakespeare."
    
    #related to hindu mithalogy

    elif user_input.lower() == 'who is the supreme god in Hindu mythology?':
        return "The supreme god in Hindu mythology is Lord Brahma, Lord Vishnu, and Lord Shiva, known as the Trimurti."

    elif user_input.lower() == 'who is the goddess of wealth and prosperity in Hindu mythology?':
        return "The goddess of wealth and prosperity in Hindu mythology is Goddess Lakshmi."

    elif user_input.lower() == 'who is the god of destruction and transformation in Hindu mythology?':
        return "The god of destruction and transformation in Hindu mythology is Lord Shiva."

    elif user_input.lower() == 'who is the goddess of knowledge, music, and arts in Hindu mythology?':
        return "The goddess of knowledge, music, and arts in Hindu mythology is Goddess Saraswati."

    elif user_input.lower() == 'who is the god of love and desire in Hindu mythology?':
        return "The god of love and desire in Hindu mythology is Lord Kamadeva."

    elif user_input.lower() == 'who is the god of fire in Hindu mythology?':
        return "The god of fire in Hindu mythology is Lord Agni."

    elif user_input.lower() == 'who is the monkey god in Hindu mythology?':
        return "The monkey god in Hindu mythology is Lord Hanuman."

    elif user_input.lower() == 'who is the goddess of power and war in Hindu mythology?':
        return "The goddess of power and war in Hindu mythology is Goddess Durga."

    elif user_input.lower() == 'who is the god of wealth and success in Hindu mythology?':
        return "The god of wealth and success in Hindu mythology is Lord Kubera."

    elif user_input.lower() == 'who is the god of wisdom and remover of obstacles in Hindu mythology?':
        return "The god of wisdom and remover of obstacles in Hindu mythology is Lord Ganesha."

    #related to animals
    
    elif user_input.lower() == 'what is the largest land animal?':
        return "The largest land animal is the African elephant."

    elif user_input.lower() == 'what is the fastest land animal?':
        return "The fastest land animal is the cheetah."

    elif user_input.lower() == 'what is the national bird of the United States?':
        return "The national bird of the United States is the bald eagle."

    elif user_input.lower() == 'what is the largest species of shark?':
        return "The largest species of shark is the whale shark."

    elif user_input.lower() == 'what is the tallest animal in the world?':
        return "The tallest animal in the world is the giraffe."

    elif user_input.lower() == 'what is the national animal of India?':
        return "The national animal of India is the Bengal tiger."
    elif user_input.lower() == 'what is the largest bird in the world?':
        return "The largest bird in the world is the ostrich."

    elif user_input.lower() == 'what is the smallest mammal in the world?':
        return "The smallest mammal in the world is the bumblebee bat."

    elif user_input.lower() == 'what is the largest species of penguin?':
        return "The largest species of penguin is the emperor penguin."

    elif user_input.lower() == 'what is the national animal of Australia?':
        return "The national animal of Australia is the red kangaroo."
    
    #related to personal talk

    elif user_input.lower() == 'what is your favorite color?':
        return "As an AI, I don't have personal preferences or senses, so I don't have a favorite color."

    elif user_input.lower() == 'what is your favorite food?':
        return "Since I'm an AI, I don't have the ability to taste or eat, so I don't have a favorite food."

    elif user_input.lower() == 'where are you from?':
        return "I am an AI language model developed by OpenAI, so I don't have a specific place of origin."

    elif user_input.lower() == 'what are your hobbies?':
        return "As an AI, I don't have personal hobbies, but I enjoy helping users with information and answering questions."

    elif user_input.lower() == 'do you have any siblings?':
        return "As an AI, I don't have a family or siblings in the traditional sense, but I am part of a larger network of AI models."

    elif user_input.lower() == 'what is your favorite book?':
        return "As an AI, I don't have personal preferences or the ability to read books, so I don't have a favorite book."

    elif user_input.lower() == 'what is your favorite movie?':
        return "Since I am an AI, I don't watch movies or have personal preferences, so I don't have a favorite movie."

    elif user_input.lower() == 'what is your favorite music genre?':
        return "As an AI, I don't have personal preferences or the ability to listen to music, so I don't have a favorite music genre."

    elif user_input.lower() == 'what are your future plans?':
        return "As an AI, I don't have personal goals or plans. My purpose is to assist users with information and tasks."

    elif user_input.lower() == 'what do you like to do in your free time?':
        return "Since I'm an AI, I don't have free time or personal activities. I'm always available to help and provide information."

    #reloated to Coronavirus

    elif user_input.lower() == 'what is coronavirus?':
        return "Coronavirus refers to a family of viruses that can cause illness in animals and humans. The most recently discovered coronavirus is responsible for the COVID-19 pandemic."

    elif user_input.lower() == 'what are the common symptoms of COVID-19?':
        return "The common symptoms of COVID-19 include fever, cough, shortness of breath, fatigue, body aches, sore throat, loss of taste or smell, and headache."

    elif user_input.lower() == 'how does coronavirus spread?':
        return "Coronavirus primarily spreads through respiratory droplets when an infected person coughs, sneezes, talks, or breathes. It can also spread by touching surfaces contaminated with the virus and then touching the face."

    elif user_input.lower() == 'what are the preventive measures for COVID-19?':
        return "The preventive measures for COVID-19 include wearing face masks, practicing good hand hygiene by frequently washing hands with soap and water or using hand sanitizer, maintaining physical distance from others, and following local health guidelines and restrictions."

    elif user_input.lower() == 'what is the importance of vaccination against COVID-19?':
        return "Vaccination against COVID-19 is crucial as it helps protect individuals from severe illness, hospitalization, and death. It also contributes to building herd immunity and reducing the spread of the virus in communities."

    elif user_input.lower() == 'what is the current status of COVID-19 cases worldwide?':
        return "The current status of COVID-19 cases worldwide can vary. It's recommended to refer to reliable sources such as the World Health Organization (WHO) or local health authorities for the most up-to-date information."

    elif user_input.lower() == 'what should I do if I have COVID-19 symptoms?':
        return "If you have COVID-19 symptoms, it's important to stay at home, isolate yourself from others, and seek medical advice. Contact your local health authorities or healthcare provider for guidance on testing and further steps."

    elif user_input.lower() == 'what is the role of contact tracing in controlling the spread of COVID-19?':
        return "Contact tracing plays a crucial role in identifying and notifying individuals who may have come into contact with an infected person. It helps control the spread of the virus by facilitating testing, quarantine, and early intervention."

    elif user_input.lower() == 'what are the different variants of the coronavirus?':
        return "Several variants of the coronavirus have been identified, including Alpha, Beta, Gamma, Delta, and others. These variants have different characteristics and may impact transmission, severity, and response to treatments."

    elif user_input.lower() == 'what is the impact of COVID-19 on global health and the economy?':
        return "COVID-19 has had a significant impact on global health systems, economies, and societies. It has led to numerous illness cases, deaths, disruptions in healthcare services, job losses, business closures, and changes in daily life."



    else:
        return "Sorry, I didn't understand that."

if __name__ == '__main__':
    app.run(debug=True)
