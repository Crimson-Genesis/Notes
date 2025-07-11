# Unit - 1 -> Introduction to Artificial Intelligence, Solving Problems by Searching and Adversial search
Introduction to Artificial Intelligence: Definition, Foundation of AI, history of AI, Task Domains of AI, Levels of Artificial Intelligence,
Applications of AI. Intlligent agents: Agents and Environments, the concepts of rationality, the nature of environments, structure of agents.
Solving Problems by Searching: Problem-solving Agents, Forulating Problems
Example problems, and searching for Solutions, uniformed search strategies - Breadth first search, depth first Search.
Search with partial information (Heuristic search) Hill climbing, Best-First Search, A*.

## Content -> 
### **Introduction to Artificial Intelligence**

---

#### **1. Definition of Artificial Intelligence (AI)**

* AI is the branch of computer science concerned with building smart machines capable of performing tasks that typically require human intelligence.
* It is the simulation of human intelligence processes by machines, especially computer systems.
* These processes include learning, reasoning, and self-correction.

---

#### **2. Foundations of AI**

* **Mathematics**

  * Logic: Propositional and first-order logic
  * Probability: Bayesian inference
  * Statistics: Data analysis and modeling
  * Linear Algebra and Calculus: For optimization and machine learning algorithms
* **Philosophy**

  * Theories of reasoning, ethics, mind-body problem
  * Concepts of consciousness and logic
* **Psychology and Cognitive Science**

  * Understanding human intelligence and behavior
  * Modeling human thought processes
* **Computer Engineering**

  * Hardware design for AI applications
  * Memory, processors, GPUs for parallel computing
* **Neuroscience**

  * Study of how the human brain works to inspire neural networks
* **Linguistics**

  * Language understanding and generation
  * Grammar, syntax, semantics for NLP systems

---

#### **3. History of AI**

* **1940s–1950s**

  * Alan Turing's “Turing Test” (1950)
  * First neural network model by McCulloch and Pitts
* **1956**

  * Term “Artificial Intelligence” coined at Dartmouth Conference
* **1960s–1970s**

  * Development of early AI programs like ELIZA (natural language) and SHRDLU (robotics)
  * Focus on symbolic AI and expert systems
* **1980s**

  * Rise of Expert Systems (e.g., MYCIN)
  * AI Winter due to high expectations and low results
* **1990s**

  * Reinforcement learning and probabilistic reasoning gains momentum
  * IBM’s Deep Blue defeated world chess champion Garry Kasparov in 1997
* **2000s**

  * Rise of data-driven AI and machine learning
* **2010s–Present**

  * Deep learning, big data, cloud computing revolutionize AI
  * AI systems like AlphaGo, GPT models, DALL·E, etc.

---

#### **4. Task Domains of AI**

* **Perception**

  * Vision (image recognition, object detection)
  * Speech (voice recognition, transcription)
* **Reasoning and Decision Making**

  * Logical inference, expert systems, planning algorithms
* **Learning**

  * Supervised, unsupervised, reinforcement learning
* **Natural Language Processing**

  * Language understanding, machine translation, sentiment analysis
* **Robotics**

  * Navigation, path planning, grasping, manipulation
* **Problem Solving**

  * Game playing, scheduling, resource allocation
* **Actuation**

  * Control systems, feedback mechanisms in physical systems

---

#### **5. Levels of Artificial Intelligence**

* **Artificial Narrow Intelligence (ANI)**

  * Specialized in one task (e.g., facial recognition, recommendation systems)
  * Most current AI systems fall under this category
* **Artificial General Intelligence (AGI)**

  * Performs any intellectual task a human can
  * Capable of understanding, learning, and applying knowledge in different contexts
  * Still theoretical
* **Artificial Super Intelligence (ASI)**

  * Surpasses human intelligence in all aspects
  * Hypothetical and not yet realized

---

#### **6. Applications of AI**

* **Healthcare**

  * Disease diagnosis, medical imaging, drug discovery
* **Finance**

  * Fraud detection, algorithmic trading, credit scoring
* **Transportation**

  * Self-driving cars, traffic prediction, route optimization
* **Retail**

  * Personalized recommendations, inventory management, chatbots
* **Agriculture**

  * Crop monitoring, precision farming, yield prediction
* **Manufacturing**

  * Predictive maintenance, quality control, robotics
* **Education**

  * Intelligent tutoring systems, automated grading, adaptive learning platforms
* **Entertainment**

  * Content recommendations, procedural content generation
* **Cybersecurity**

  * Threat detection, malware analysis, automated response
* **Smart Assistants**

  * Siri, Alexa, Google Assistant
* **Military**

  * Surveillance, autonomous drones, decision support systems

---

#### **7. Intelligent Agents**

* **Agents and Environments**

  * **Agent:** An entity that perceives its environment and acts upon it
  * **Environment:** The external context in which an agent operates
* **Percepts:** Input received from the environment
* **Actions:** Responses or outputs given by the agent

---

#### **8. Concept of Rationality**

* A rational agent selects actions that maximize its performance measure based on:

  * The percept sequence
  * Its knowledge of the environment
  * Possible actions
* Rationality ≠ Omniscience (agent cannot predict future perfectly)

---

#### **9. Nature of Environments**

* **Observable vs. Partially Observable**

  * Full access to environment state vs. incomplete information
* **Deterministic vs. Stochastic**

  * Next state determined solely by current state and action vs. involving randomness
* **Episodic vs. Sequential**

  * Tasks are divided into independent episodes vs. decisions affecting future
* **Static vs. Dynamic**

  * Environment remains unchanged while the agent deliberates vs. changing
* **Discrete vs. Continuous**

  * Finite number of actions/percepts vs. infinite
* **Single-Agent vs. Multi-Agent**

  * One agent acting alone vs. presence of other agents

---

#### **10. Structure of Agents**

* **Simple Reflex Agents**

  * Act based on current percept only using condition-action rules
* **Model-Based Reflex Agents**

  * Maintain internal state to handle partially observable environments
* **Goal-Based Agents**

  * Use goal information to guide actions
* **Utility-Based Agents**

  * Use a utility function to measure performance and make trade-offs
* **Learning Agents**

  * Improve performance over time based on experiences

---
### **Definition of Artificial Intelligence (AI)**

1. **Basic Definition**

   * Artificial Intelligence is the branch of computer science concerned with creating systems that can perform tasks that normally require human intelligence.

2. **Formal Definition**

   * AI is the science and engineering of making intelligent machines, especially intelligent computer programs, capable of performing tasks such as learning, reasoning, problem-solving, perception, and language understanding.

3. **Functional Definition**

   * AI enables machines to mimic cognitive functions such as:

     * Learning from experience (data)
     * Understanding natural language
     * Recognizing patterns
     * Making decisions
     * Solving problems

4. **Turing Test-Based Definition**

   * According to Alan Turing, a machine is considered intelligent if it can exhibit behavior indistinguishable from that of a human in a conversation (Turing Test).

5. **Categories Based on Thinking and Acting**

   * **Thinking Humanly:** Machines that simulate human thought processes.
   * **Acting Humanly:** Machines that behave like humans.
   * **Thinking Rationally:** Machines that reason logically to reach conclusions.
   * **Acting Rationally:** Machines that take actions to achieve specific goals optimally.

6. **Types of Intelligence Simulated**

   * **Cognitive Intelligence:** Learning, memory, problem-solving
   * **Emotional Intelligence:** Understanding emotions (limited)
   * **Perceptual Intelligence:** Visual and auditory perception

7. **Scope**

   * AI includes various subfields:

     * Machine Learning
     * Natural Language Processing
     * Robotics
     * Expert Systems
     * Computer Vision
     * Planning and Scheduling

8. **Goal of AI**

   * To create systems that can function autonomously, adapt to new situations, and improve over time through experience or data.

### **Foundations of Artificial Intelligence (AI)**

---

#### **1. Mathematics**

* **Logic**

  * Propositional Logic: Deals with true/false values using logical connectives (AND, OR, NOT).
  * First-Order Logic: Allows use of quantifiers (∀, ∃) and predicates to express complex statements.
* **Probability Theory**

  * Used for reasoning under uncertainty.
  * Includes Bayesian Networks and Markov Models.
* **Statistics**

  * Inference from data, hypothesis testing, regression, distributions.
  * Crucial for supervised and unsupervised learning.
* **Linear Algebra**

  * Vectors, matrices, and operations essential for neural networks and computer vision.
* **Calculus**

  * Differentiation and gradients used in optimization techniques like gradient descent.

---

#### **2. Philosophy**

* **Epistemology**

  * Study of knowledge, belief, and justification; used in AI for knowledge representation.
* **Logic**

  * Basis for reasoning systems and formal argument structure.
* **Ethics**

  * Provides framework for discussing consequences and responsibility of AI systems.
* **Consciousness and Mind-Body Problem**

  * Influences debates on machine consciousness and intelligence.

---

#### **3. Psychology and Cognitive Science**

* **Human Learning and Thinking**

  * Models of human cognition inspire learning algorithms.
* **Problem Solving and Decision Making**

  * Psychological experiments inform how humans approach tasks, aiding in heuristic design.
* **Cognitive Architectures**

  * Frameworks like ACT-R and SOAR simulate human cognition for agent design.

---

#### **4. Computer Engineering**

* **Hardware Design**

  * Creation of processors and memory systems optimized for AI tasks.
  * Includes GPUs, TPUs, and specialized AI chips.
* **Parallel and Distributed Computing**

  * Facilitates handling of large-scale computations for AI models.
* **Embedded Systems**

  * Used in robotics and real-time AI systems.

---

#### **5. Neuroscience**

* **Brain Function Modeling**

  * Artificial Neural Networks (ANNs) are inspired by the structure of the human brain.
* **Synaptic Learning**

  * Biological learning mechanisms (Hebbian theory) influence algorithms like backpropagation.
* **Neuroplasticity**

  * Informs adaptable and dynamic learning models.

---

#### **6. Linguistics**

* **Syntax and Grammar**

  * Rule-based sentence construction used in natural language processing (NLP).
* **Semantics**

  * Understanding meaning behind words and sentences.
* **Pragmatics**

  * Deals with contextual meaning and conversational inference.
* **Computational Linguistics**

  * Provides models and tools for parsing, tagging, machine translation, and dialogue systems.

---

#### **7. Economics**

* **Utility Theory**

  * Used for decision-making agents to maximize rewards.
* **Game Theory**

  * Helps in designing AI strategies in competitive and cooperative multi-agent environments.
* **Market Modeling**

  * AI applied to simulations of supply-demand, auctions, and resource allocation.

---

#### **8. Control Theory**

* **Feedback Systems**

  * Agents adjust actions based on environmental responses (closed-loop systems).
* **Optimization and Stability**

  * Ensures robustness of AI models in dynamic and uncertain environments.

---

#### **9. Linguistic Philosophy**

* **Symbolic Representation**

  * Use of symbols and formal language to express knowledge and logic.
* **Semantic Networks**

  * Relational knowledge representation structures influenced by philosophical models of meaning.

---

#### **10. Education and Learning Sciences**

* **Learning Theories**

  * Rote learning, conceptual learning, experiential learning, which inform machine learning strategies.
* **Assessment and Evaluation**

  * Applied in AI-based intelligent tutoring systems and adaptive learning technologies.

---
### **History of Artificial Intelligence (AI)**

---

#### **1. Pre-20th Century: Origins and Early Ideas**

* **Ancient Myths and Automatons**

  * Myths of artificial beings (e.g., Talos of Crete, Golem) suggested early interest in synthetic intelligence.
* **Mechanical Devices**

  * 13th century: Al-Jazari’s programmable automaton.
  * 17th century: Pascal’s mechanical calculator.
* **Philosophical Foundations**

  * René Descartes: “I think, therefore I am” – explored ideas of mind and intelligence.
  * Leibniz: Concept of a formal logical language.

---

#### **2. 1940s–1950s: Birth of Modern AI**

* **1943:** McCulloch and Pitts Model

  * Proposed first mathematical model of a neural network.
* **1950:** Alan Turing

  * Published “Computing Machinery and Intelligence.”
  * Introduced the **Turing Test** as a measure of machine intelligence.
* **1951:** Marvin Minsky and Dean Edmonds

  * Built the first neural network computer: SNARC.
* **1956:** Dartmouth Conference

  * Coined the term **“Artificial Intelligence.”**
  * Organized by John McCarthy, Marvin Minsky, Nathaniel Rochester, and Claude Shannon.
  * Marked the official beginning of AI as a field.

---

#### **3. 1956–1970: Early Enthusiasm and Symbolic AI**

* **Symbolic AI (Good Old-Fashioned AI - GOFAI)**

  * AI focused on manipulating symbols using logical rules.
* **Early Programs**

  * **Logic Theorist (1956):** First AI program by Allen Newell and Herbert Simon.
  * **General Problem Solver (1959):** Designed to solve a wide range of problems.
* **LISP Language**

  * Developed by John McCarthy in 1958; became the dominant AI language.
* **ELIZA (1964–1966)**

  * Natural language processing program simulating a psychotherapist (Joseph Weizenbaum).
* **SHRDLU (1968–1970)**

  * NLP program capable of interacting with objects in a virtual world.

---

#### **4. 1970–1980: Knowledge-Based Systems and First AI Winter**

* **Expert Systems**

  * Rule-based systems that emulate decision-making of human experts.
  * **DENDRAL:** Used for chemical analysis.
  * **MYCIN:** Diagnosed bacterial infections.
* **Limitations**

  * High cost of development.
  * Systems lacked learning capability.
* **First AI Winter (1974–1980)**

  * Funding cuts due to failure to meet exaggerated expectations.
  * Labeled as the first "AI Winter."

---

#### **5. 1980–1987: Rise of Expert Systems**

* **Commercial Success**

  * Companies began adopting expert systems for specific domains.
* **XCON System**

  * Used by DEC for computer configuration; major success story.
* **AI in Industry**

  * Japanese Fifth Generation Computer Project (FGCS) launched in 1982.

---

#### **6. 1987–1993: Second AI Winter**

* **Problems Faced**

  * Expert systems proved brittle and costly to maintain.
  * Performance degraded in real-world environments.
* **AI Disillusionment**

  * Loss of confidence in symbolic AI approaches.
  * Collapse of LISP machine market.
* **Funding Withdrawn**

  * Reduced government and industrial interest.

---

#### **7. 1993–2010: Emergence of Machine Learning and Probabilistic Models**

* **Shift from Symbolic AI to Data-Driven AI**

  * Focus on algorithms that learn from data.
* **Bayesian Networks**

  * Used for reasoning under uncertainty.
* **Support Vector Machines (SVM)**

  * Powerful classification technique introduced.
* **Reinforcement Learning**

  * Gained popularity through applications in robotics and control.
* **Milestones**

  * **1997:** IBM’s **Deep Blue** defeated chess champion Garry Kasparov.
  * **2002:** Roomba robot vacuum released – simple AI for navigation.
  * **2006:** Geoffrey Hinton coined the term **“Deep Learning.”**

---

#### **8. 2010–Present: Deep Learning Revolution**

* **Big Data and GPUs**

  * Massive datasets and powerful computation enabled deep neural networks.
* **Deep Neural Networks**

  * Outperformed traditional methods in speech, vision, and language.
* **Breakthroughs**

  * **2011:** IBM **Watson** won Jeopardy!
  * **2012:** AlexNet won ImageNet challenge – breakthrough in image recognition.
  * **2014:** **Generative Adversarial Networks (GANs)** introduced.
  * **2016:** DeepMind’s **AlphaGo** defeated world champion Lee Sedol in Go.
  * **2020–2023:** Transformer models (e.g., GPT-3, GPT-4, ChatGPT) revolutionized NLP.
* **Applications**

  * Self-driving cars, facial recognition, medical diagnostics, language translation, content generation.

---

#### **9. Current Trends (2020s)**

* **Generative AI**

  * Language and image models (ChatGPT, DALL·E, MidJourney).
* **AI in Healthcare, Law, and Finance**

  * Used in diagnostics, legal document analysis, fraud detection.
* **Ethics and Regulation**

  * Rise in discussions around fairness, transparency, and control.
* **Multimodal AI**

  * Combining text, image, audio understanding in single models.
* **Foundation Models**

  * Large-scale models trained on massive data across domains.

---

#### **10. Future Directions**

* **Artificial General Intelligence (AGI)**

  * Aim to develop machines with human-level cognitive abilities.
* **Neuromorphic Computing**

  * Hardware inspired by the human brain for energy-efficient AI.
* **Explainable AI (XAI)**

  * Creating interpretable models for critical decision-making.
* **Ethical and Responsible AI**

  * Ensuring bias-free, accountable, and safe AI systems.

### **Task Domains of Artificial Intelligence (AI)**

---

#### **1. Perception**

* **Definition:** Ability of a system to interpret data from the environment using sensory inputs.
* **Types:**

  * **Visual Perception:** Object detection, image classification, face recognition, video analysis.
  * **Speech Perception:** Speech recognition and processing.
  * **Auditory Perception:** Sound analysis and interpretation.
  * **Tactile Perception:** Physical contact sensing (used in robotics).
* **Applications:**

  * Self-driving cars (camera and LIDAR)
  * Medical imaging diagnostics
  * Surveillance systems

---

#### **2. Natural Language Processing (NLP)**

* **Definition:** Enabling machines to understand, interpret, and generate human languages.
* **Subtasks:**

  * Syntax Analysis (parsing, POS tagging)
  * Semantics (meaning extraction)
  * Sentiment Analysis
  * Machine Translation
  * Speech-to-Text and Text-to-Speech
* **Applications:**

  * Chatbots, virtual assistants (Siri, Alexa)
  * Language translation tools (Google Translate)
  * Automated summarization

---

#### **3. Reasoning and Decision Making**

* **Definition:** Deriving logical conclusions or decisions based on available knowledge or data.
* **Types:**

  * Deductive Reasoning: From general to specific.
  * Inductive Reasoning: From specific to general.
  * Abductive Reasoning: Inference to the best explanation.
* **Decision-making Strategies:**

  * Rule-based Systems
  * Probabilistic Reasoning (Bayesian Networks)
  * Fuzzy Logic Systems
* **Applications:**

  * Medical diagnosis
  * Fraud detection
  * Risk assessment

---

#### **4. Learning**

* **Definition:** Ability to improve performance from data or experience without explicit programming.
* **Types:**

  * **Supervised Learning:** Uses labeled data (e.g., classification, regression).
  * **Unsupervised Learning:** Finds hidden patterns in unlabeled data (e.g., clustering, dimensionality reduction).
  * **Reinforcement Learning:** Learning via rewards and punishments in an environment.
* **Applications:**

  * Spam detection
  * Product recommendations
  * Game playing (AlphaGo, Deep Q-Learning)

---

#### **5. Planning and Scheduling**

* **Definition:** Generating a sequence of actions to achieve specific goals under constraints.
* **Types:**

  * **Planning:** Long-term objective-driven action generation.
  * **Scheduling:** Allocating tasks and resources over time.
* **Techniques:**

  * Goal Stack Planning
  * Constraint Satisfaction
  * Hierarchical Task Networks (HTNs)
* **Applications:**

  * Robotics path planning
  * Job-shop scheduling
  * Space mission planning

---

#### **6. Robotics and Motion Control**

* **Definition:** Building autonomous systems that interact with the physical world.
* **Components:**

  * Robot hardware (sensors, actuators)
  * Robotic Perception (localization, mapping)
  * Motion Planning (trajectory computation)
  * Robot Control (feedback systems)
* **Applications:**

  * Industrial automation
  * Autonomous vehicles
  * Medical robots

---

#### **7. Problem Solving**

* **Definition:** Finding solutions to well-defined or ill-defined problems.
* **Types:**

  * Search-based problem solving (e.g., BFS, DFS, A\*)
  * Constraint-based problem solving
* **Example Problems:**

  * Puzzle solving (e.g., 8-puzzle)
  * Pathfinding (e.g., maze navigation)
  * Game playing (e.g., chess, Go)

---

#### **8. Knowledge Representation and Reasoning (KRR)**

* **Definition:** Representing information in a form that a computer system can utilize to solve complex tasks.
* **Techniques:**

  * Semantic Networks
  * Frames
  * Ontologies
  * Propositional and First-Order Logic
* **Applications:**

  * Expert systems
  * Natural language understanding
  * Semantic web

---

#### **9. Vision**

* **Definition:** Enabling machines to interpret and understand visual information from the world.
* **Subfields:**

  * Object recognition
  * Scene understanding
  * Image segmentation
* **Applications:**

  * Facial recognition systems
  * Quality inspection in manufacturing
  * Autonomous vehicle navigation

---

#### **10. Interaction and Human-AI Collaboration**

* **Definition:** Ensuring smooth and intelligent interactions between humans and AI systems.
* **Elements:**

  * User Interface (UI) and User Experience (UX)
  * Emotion recognition
  * Conversational agents
* **Applications:**

  * Customer service chatbots
  * AI assistants
  * Human-robot collaboration in manufacturing

---

#### **11. Social and Ethical Reasoning**

* **Definition:** Incorporating societal norms, values, and ethics into AI decision-making processes.
* **Areas:**

  * Bias detection and mitigation
  * Fairness and accountability
  * Legal and moral reasoning
* **Applications:**

  * AI ethics tools
  * Responsible AI frameworks
  * Compliance checking systems

---

#### **12. Game Playing**

* **Definition:** Simulating and solving strategic interactions or competitive tasks.
* **Methods:**

  * Minimax algorithm
  * Alpha-beta pruning
  * Monte Carlo Tree Search
* **Applications:**

  * Chess, Go, Poker bots
  * Strategy game AIs
  * Simulation-based training environments

---

#### **13. Expert Systems**

* **Definition:** AI systems designed to replicate the decision-making ability of human experts.
* **Components:**

  * Knowledge Base
  * Inference Engine
  * User Interface
* **Applications:**

  * Medical diagnosis systems
  * Legal reasoning tools
  * Engineering fault detection systems

---
### **Levels of Artificial Intelligence (AI)**

---

#### **1. Artificial Narrow Intelligence (ANI)**

* **Also Known As:** Weak AI
* **Definition:** AI that is specialized and designed to perform a single specific task or a narrow set of tasks.
* **Characteristics:**

  * Operates within a predefined and limited context.
  * Cannot perform tasks outside its trained domain.
  * No self-awareness or consciousness.
  * Follows human-defined rules or data-driven learning.
* **Techniques Used:**

  * Rule-based systems
  * Machine learning models
  * Natural language processing tools
* **Examples:**

  * Email spam filters
  * Siri, Alexa, Google Assistant
  * Facial recognition systems
  * Recommendation engines (Netflix, Amazon)
  * Chatbots and voice assistants
* **Current Status:**

  * All existing AI systems are ANI.

---

#### **2. Artificial General Intelligence (AGI)**

* **Also Known As:** Strong AI or Human-Level AI
* **Definition:** AI that possesses the ability to understand, learn, and apply knowledge in a manner equivalent to a human being across a wide range of tasks.
* **Characteristics:**

  * Can perform any intellectual task that a human can do.
  * Capable of transferring knowledge from one domain to another.
  * Has reasoning, problem-solving, learning, planning, and language understanding abilities.
  * Possesses self-awareness and adaptability.
* **Research Challenges:**

  * True understanding and reasoning
  * Long-term memory and knowledge transfer
  * Common sense reasoning
  * Creativity and abstract thinking
* **Examples:**

  * No real-world example exists as of now.
  * Theoretical models, fictional portrayals (e.g., Data from Star Trek, HAL 9000 from 2001: A Space Odyssey).
* **Current Status:**

  * Not yet achieved; active area of research.

---

#### **3. Artificial Super Intelligence (ASI)**

* **Also Known As:** Superintelligent AI
* **Definition:** AI that surpasses human intelligence in all aspects, including creativity, decision-making, emotional intelligence, and problem-solving.
* **Characteristics:**

  * Far more capable than the best human minds.
  * Can outperform humans in every field (science, mathematics, arts, etc.).
  * Possesses high-level self-awareness and consciousness.
  * Capable of self-improvement, learning at superhuman speeds.
* **Risks and Concerns:**

  * Ethical and moral concerns.
  * Control and alignment problems.
  * Existential risks to humanity if misaligned.
* **Examples:**

  * Hypothetical; no current system qualifies.
  * Depicted in science fiction (e.g., Skynet in Terminator, Ultron in Marvel Universe).
* **Current Status:**

  * Entirely speculative and theoretical.

---

#### **4. Summary Table**

| **Level** | **Also Known As** | **Capability**                            | **Examples**                            | **Status**         |
| --------- | ----------------- | ----------------------------------------- | --------------------------------------- | ------------------ |
| ANI       | Weak AI           | Narrow tasks only                         | Siri, Alexa, Google Translate, Chess AI | Fully developed    |
| AGI       | Strong AI         | Human-like intelligence across domains    | None (hypothetical)                     | Not yet developed  |
| ASI       | Superintelligence | Exceeds human intelligence in all aspects | None (theoretical)                      | Future possibility |

---
### **Applications of Artificial Intelligence (AI)**

---

#### **1. Healthcare**

* **Medical Diagnosis**

  * AI analyzes symptoms and diagnostic data to identify diseases (e.g., cancer, pneumonia).
* **Medical Imaging**

  * AI interprets CT, MRI, and X-rays using image recognition algorithms.
* **Drug Discovery**

  * AI models predict molecule behavior, reducing time and cost in R\&D.
* **Virtual Health Assistants**

  * Chatbots provide symptom checking and medical guidance.
* **Personalized Medicine**

  * AI recommends treatments based on patient history and genetics.

---

#### **2. Finance**

* **Fraud Detection**

  * AI detects unusual transactions using anomaly detection algorithms.
* **Algorithmic Trading**

  * High-frequency trading based on market data predictions.
* **Credit Scoring**

  * Machine learning models assess credit risk based on applicant data.
* **Chatbots for Banking**

  * AI agents handle customer service and basic banking queries.

---

#### **3. Transportation**

* **Autonomous Vehicles**

  * Self-driving cars use AI for perception, planning, and control.
* **Traffic Prediction**

  * AI forecasts traffic flow using historical and real-time data.
* **Route Optimization**

  * AI suggests optimal travel routes based on congestion patterns.
* **Fleet Management**

  * AI monitors and coordinates transportation fleets.

---

#### **4. Retail and E-Commerce**

* **Recommendation Engines**

  * Suggests products based on user preferences and behavior.
* **Customer Service**

  * AI-powered chatbots resolve queries and support ticket systems.
* **Inventory Management**

  * Predicts product demand and automates stock replenishment.
* **Visual Search**

  * Allows searching for products using images instead of text.

---

#### **5. Education**

* **Intelligent Tutoring Systems**

  * AI adapts teaching content to individual student learning styles.
* **Automated Grading**

  * Evaluates multiple-choice and short-answer questions.
* **Learning Analytics**

  * Tracks student performance and engagement to personalize learning.
* **Language Learning Tools**

  * AI supports vocabulary, pronunciation, and grammar correction.

---

#### **6. Manufacturing**

* **Predictive Maintenance**

  * AI predicts equipment failure using sensor data.
* **Quality Control**

  * Uses computer vision to detect product defects.
* **Robotic Process Automation (RPA)**

  * Automates repetitive industrial tasks.
* **Supply Chain Optimization**

  * AI forecasts demand and manages resources.

---

#### **7. Agriculture**

* **Precision Farming**

  * AI analyzes soil data and crop health for optimized farming.
* **Yield Prediction**

  * Machine learning models estimate crop production.
* **Weed and Pest Detection**

  * Image recognition identifies harmful organisms.
* **Autonomous Tractors and Drones**

  * AI controls machinery for planting, spraying, and monitoring.

---

#### **8. Cybersecurity**

* **Threat Detection**

  * AI identifies malware, phishing, and intrusion patterns.
* **User Behavior Analytics**

  * Detects anomalous user activities indicating a security breach.
* **Automated Incident Response**

  * AI recommends or executes countermeasures to cyberattacks.

---

#### **9. Entertainment and Media**

* **Content Recommendation**

  * Suggests movies, songs, or news (e.g., Netflix, Spotify).
* **Game AI**

  * NPCs and enemies controlled by intelligent systems.
* **Content Generation**

  * AI creates music, art, and stories (e.g., generative models).
* **Deepfakes**

  * AI-generated audio/video mimicking real people.

---

#### **10. Smart Assistants**

* **Virtual Personal Assistants**

  * Voice-activated AI like Siri, Alexa, Google Assistant.
* **Home Automation**

  * AI controls lighting, temperature, and appliances.
* **Voice Commands**

  * AI understands and responds to spoken instructions.

---

#### **11. Military and Defense**

* **Autonomous Drones**

  * Perform surveillance and reconnaissance.
* **Decision Support Systems**

  * AI analyzes battlefield data for strategic planning.
* **Cyber Defense**

  * Protects military networks using AI-driven threat detection.

---

#### **12. Legal Sector**

* **Contract Analysis**

  * AI extracts and reviews legal clauses.
* **Legal Research**

  * AI identifies relevant case laws and precedents.
* **Predictive Judgments**

  * Forecasts case outcomes based on historical data.

---

#### **13. Human Resources**

* **Resume Screening**

  * AI filters and ranks job applications.
* **Employee Monitoring**

  * Analyzes productivity and engagement.
* **Chatbots for Recruitment**

  * Interacts with candidates and schedules interviews.

---

#### **14. Space Exploration**

* **Autonomous Rovers**

  * AI navigates planetary terrain (e.g., Mars rovers).
* **Satellite Image Analysis**

  * Interprets space-based data for climate and terrain mapping.
* **Mission Planning**

  * AI helps design and simulate space missions.

---

#### **15. Smart Cities**

* **Surveillance Systems**

  * AI analyzes video feeds for public safety.
* **Energy Management**

  * Optimizes power usage using predictive algorithms.
* **Smart Traffic Lights**

  * AI adapts signals based on traffic density.

---

#### **16. Environmental Monitoring**

* **Wildlife Tracking**

  * AI analyzes images and sensor data for conservation.
* **Climate Modeling**

  * Predicts weather and climate trends using simulation.
* **Pollution Detection**

  * Identifies sources and levels of air and water pollution.

---
### **Intelligent Agents**

---

#### **1. Definition**

* An **intelligent agent** is an autonomous entity that observes its environment through sensors, acts upon that environment through actuators, and uses some form of intelligence to make decisions that maximize its performance over time.

---

#### **2. Agent Function**

* An agent function maps any given percept (input from the environment) to an action.
* It is represented as:
  **f: P\* → A**
  where P\* is the set of percept sequences, and A is the set of actions.

---

#### **3. Structure of Intelligent Agents**

* **Sensors:** Components through which the agent perceives the environment (e.g., camera, microphone).
* **Actuators:** Mechanisms through which the agent acts upon the environment (e.g., wheels, robotic arms).
* **Percepts:** Inputs received at a given moment from the environment.
* **Percept Sequence:** Entire history of everything the agent has perceived.
* **Performance Measure:** Criteria used to evaluate agent's behavior (e.g., speed, accuracy, efficiency).
* **Agent Program:** Software that implements the agent function and determines actions based on percepts.

---

#### **4. Types of Intelligent Agents**

* **Simple Reflex Agents**

  * Respond directly to percepts using condition-action rules.
  * Do not consider the history of percepts or future consequences.
  * Example: Thermostat system.

* **Model-Based Reflex Agents**

  * Maintain internal state based on percept history.
  * Model of the world helps in decision making for partially observable environments.

* **Goal-Based Agents**

  * Act to achieve explicit goals.
  * Use search and planning to reach goals.

* **Utility-Based Agents**

  * Use a utility function to measure performance of each state.
  * Make decisions based on maximizing expected utility.

* **Learning Agents**

  * Improve their performance over time by learning from experience.
  * Include learning elements and performance elements.

---

#### **5. Rationality**

* **Definition:** A rational agent chooses actions that maximize its performance measure based on percept history and built-in knowledge.
* **Properties:**

  * Rationality is not the same as perfection.
  * Rational agent acts appropriately with incomplete information and limited resources.
  * Rationality depends on:

    * The performance measure
    * The agent’s prior knowledge
    * The actions the agent can perform
    * The agent’s percept sequence to date

---

#### **6. PEAS Framework (for Designing Agents)**

* **P**: Performance Measure – Defines the success criteria.
* **E**: Environment – The external context in which the agent operates.
* **A**: Actuators – Tools used by the agent to act on the environment.
* **S**: Sensors – Devices used to perceive the environment.

**Example (Self-driving Car):**

* **Performance Measure** – Safety, time, fuel efficiency, legality.
* **Environment** – Roads, traffic, pedestrians, weather.
* **Actuators** – Steering, brakes, accelerator.
* **Sensors** – Cameras, GPS, radar, lidar.

---

#### **7. Environments of Intelligent Agents**

* **Fully Observable vs. Partially Observable**

  * Fully observable: Agent's sensors give complete information (e.g., chess game).
  * Partially observable: Some state info is hidden (e.g., driving in fog).

* **Deterministic vs. Stochastic**

  * Deterministic: Outcomes are predictable (e.g., tic-tac-toe).
  * Stochastic: Outcomes are uncertain (e.g., poker).

* **Episodic vs. Sequential**

  * Episodic: Each action is independent (e.g., image classification).
  * Sequential: Actions are interdependent (e.g., chess).

* **Static vs. Dynamic**

  * Static: Environment does not change while agent is deciding (e.g., crossword).
  * Dynamic: Environment changes over time (e.g., stock market).

* **Discrete vs. Continuous**

  * Discrete: Finite number of states and actions (e.g., board games).
  * Continuous: Infinite states/actions (e.g., driving).

* **Single-Agent vs. Multi-Agent**

  * Single-agent: Only one agent (e.g., solitaire).
  * Multi-agent: Multiple agents acting (e.g., soccer game with AI players).

---

#### **8. Examples of Intelligent Agents**

* **Software Agents**

  * Spam filters, recommendation systems, AI tutors.
* **Robotic Agents**

  * Autonomous drones, vacuum cleaners (e.g., Roomba), industrial robots.
* **Embedded AI Agents**

  * Smart thermostats, self-parking cars, home assistants.

---
### **Agents and Environments**

---

#### **1. Agent**

* An **agent** is an autonomous entity that perceives its environment through **sensors** and acts upon the environment using **actuators**.
* It uses an **agent program** to determine what action to take based on the current **percept** or **percept sequence**.

---

#### **2. Environment**

* The **environment** is the external world with which the agent interacts.
* It provides **percepts** to the agent and receives **actions** from the agent.

---

#### **3. Components of an Agent**

* **Sensors** – Receive input from the environment (e.g., cameras, microphones).
* **Actuators** – Perform actions on the environment (e.g., motors, speakers).
* **Percept** – The current input from the environment.
* **Percept Sequence** – The complete history of all percepts received so far.
* **Agent Function** – A mapping from percept sequences to actions.

  * $f: P^* \rightarrow A$
* **Agent Program** – Implements the agent function using computation.

---

#### **4. Types of Environments**

| **Property**      | **Description**                                                          | **Examples**                                               |
| ----------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------- |
| **Observable**    | Fully (complete access to environment state) or Partially (limited view) | Fully: Chess game; Partially: Poker                        |
| **Deterministic** | Outcome of actions is predictable                                        | Deterministic: Board games; Stochastic: Autonomous driving |
| **Episodic**      | Current action independent of past actions                               | Episodic: Image classification                             |
| **Static**        | Does not change while agent is reasoning                                 | Static: Crossword puzzles; Dynamic: Driving                |
| **Discrete**      | Finite number of actions/percepts                                        | Discrete: Turn-based games                                 |
| **Single-agent**  | Agent operates alone or with other agents                                | Single-agent: Solitaire; Multi-agent: Football game        |

---

#### **5. Agent-Environment Interaction Cycle**

* Step 1: Agent **senses** the environment via sensors (receives a percept).
* Step 2: Agent uses its program to decide on an **action** based on percept history.
* Step 3: Agent **acts** using actuators.
* Step 4: Environment **responds** to the action (may change state).
* Step 5: New **percept** is received by the agent → cycle repeats.

---

#### **6. PEAS Framework (used to specify agent task)**

* **P – Performance Measure:** Criteria for success (e.g., safety, speed).
* **E – Environment:** The world agent operates in (e.g., roads, weather).
* **A – Actuators:** Tools to act (e.g., wheels, brakes).
* **S – Sensors:** Tools to perceive (e.g., cameras, GPS).

**Example: Self-Driving Car**

| Component   | Details                                    |
| ----------- | ------------------------------------------ |
| Performance | Safety, legality, fuel efficiency, comfort |
| Environment | Roads, traffic, pedestrians, weather       |
| Actuators   | Steering wheel, throttle, brake            |
| Sensors     | Lidar, radar, camera, GPS                  |

---

#### **7. Types of Environments in Detail**

* **Fully Observable vs. Partially Observable**

  * Fully: Agent has access to complete environment state at any time.
  * Partially: Agent only has limited or noisy information about the state.

* **Deterministic vs. Stochastic**

  * Deterministic: Next state is completely determined by current state and action.
  * Stochastic: Environment has randomness or uncertainty.

* **Episodic vs. Sequential**

  * Episodic: Each action's outcome is independent.
  * Sequential: Actions affect future states.

* **Static vs. Dynamic**

  * Static: Environment does not change while agent is thinking.
  * Dynamic: Environment can change independently or over time.

* **Discrete vs. Continuous**

  * Discrete: Finite number of distinct states/actions.
  * Continuous: Infinite states/actions, often involving real numbers.

* **Single-Agent vs. Multi-Agent**

  * Single-Agent: Agent acts independently.
  * Multi-Agent: Other agents exist; may be cooperative or competitive.

---

#### **8. Examples of Agents and Their Environments**

| **Agent**              | **Environment**                                   |
| ---------------------- | ------------------------------------------------- |
| Robotic Vacuum Cleaner | Floor layout, furniture, obstacles                |
| Chess Program          | Chessboard and opponent’s moves                   |
| Web Crawler            | Internet websites and hyperlinks                  |
| Medical Diagnosis AI   | Patient data, lab reports                         |
| Autonomous Drone       | Sky, weather, GPS signals, objects in flight path |

---
### **Agents vs Environments**

---

| **Aspect**                     | **Agent**                                                          | **Environment**                                                        |
| ------------------------------ | ------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| **Definition**                 | An autonomous entity that perceives and acts in the environment    | The external context or world in which the agent operates              |
| **Role**                       | Makes decisions and performs actions to achieve goals              | Provides percepts to the agent and responds to its actions             |
| **Components**                 | Sensors, Actuators, Agent Program, Percept Sequence                | Objects, settings, events, and phenomena the agent interacts with      |
| **Input/Perception**           | Receives percepts via sensors                                      | Generates percepts based on its current state or external changes      |
| **Output/Action**              | Executes actions through actuators                                 | Changes its state or provides feedback based on agent's actions        |
| **Goal**                       | Maximize performance measure through intelligent behavior          | Reacts to or supports agent behavior within defined rules and dynamics |
| **Dependence**                 | Depends on environment for percepts and action results             | Can be independent or affected by one or multiple agents               |
| **Example (Self-Driving Car)** | Car with sensors and software controlling steering, speed, braking | Roads, traffic, pedestrians, weather                                   |
| **Example (Chess AI)**         | Software that makes moves based on game state                      | Chessboard, opponent moves                                             |
| **Interaction**                | Continuously senses, thinks, and acts                              | Continuously provides percepts and changes based on actions taken      |

---

### **Summary**

* **Agents** are active, goal-directed systems.
* **Environments** are passive contexts within which agents function.
* Agents **sense** the environment and **act** upon it to fulfill tasks.
* Environments **provide information** and **react** to actions, shaping future agent behavior.

---
### **The Concepts of Rationality in Artificial Intelligence**

---

#### **1. Definition of Rationality**

* **Rationality** refers to the ability of an agent to make decisions and perform actions that maximize its **performance measure** based on:

  * The **percept history**
  * The **agent's built-in knowledge**
  * The **actions available to it**

---

#### **2. Rational Agent**

* A **rational agent** is one that acts to achieve the best expected outcome (or to maximize utility) based on what it perceives and knows.

---

#### **3. Characteristics of Rationality**

* **Depends on Four Factors:**

  1. **Performance Measure** – The criterion to judge the success of the agent.
  2. **Percept Sequence** – The entire history of what the agent has perceived.
  3. **Knowledge** – The information the agent has about the environment.
  4. **Available Actions** – The set of actions the agent can perform.

* **Not the Same as Omniscience:**

  * Rationality does **not** require complete knowledge of the future or environment.
  * The agent makes the best possible decision with **limited** information.

* **Involves Exploration:**

  * Rational agents may explore to gather more information to improve future decisions.

* **Outcome vs. Decision:**

  * Rationality is judged **by the decision-making process**, not by the actual outcome.
  * A rational action might lead to a bad outcome due to unexpected changes, but the decision was still rational.

---

#### **4. Rational vs. Irrational Behavior**

* **Rational Behavior:** Chooses the most suitable action based on goal, current percept, and available knowledge.
* **Irrational Behavior:** Ignores information, chooses randomly or acts against the performance measure.

---

#### **5. Rationality in Different Types of Agents**

* **Simple Reflex Agents:** Rational only in fully observable environments with direct mapping of percepts to actions.
* **Model-Based Reflex Agents:** More rational as they maintain internal state of unobservable parts of environment.
* **Goal-Based Agents:** Rationality based on evaluating and choosing actions that move toward the goal.
* **Utility-Based Agents:** Rationality includes choosing among multiple goals or conflicting objectives using utility functions.
* **Learning Agents:** Improve rationality over time by learning from experience.

---

#### **6. Perfect Rationality vs. Bounded Rationality**

* **Perfect Rationality:**

  * Makes the optimal decision always.
  * Assumes unlimited time and computational power.
* **Bounded Rationality:**

  * Makes the best decision within the **limits of resources** (time, computation, knowledge).
  * More realistic model for practical AI agents.

---

#### **7. Example**

**Self-Driving Car Agent:**

* **Percepts:** GPS data, traffic signals, road obstacles.
* **Performance Measure:** Reach destination safely and quickly.
* **Rational Action:** Slowing down for a red light or avoiding a pedestrian.
* **Irrational Action:** Ignoring the red light or taking a longer route without benefit.

---

#### **8. Summary**

* Rationality is the core concept that governs how an AI agent should act.
* Rational agents:

  * Use percepts, actions, and internal knowledge.
  * Maximize performance measure.
  * Adapt behavior based on environment and learning.

---
### **The Nature of Environments in Artificial Intelligence**

---

An **environment** is everything outside the agent that the agent interacts with. The nature of environments significantly affects the design, performance, and behavior of intelligent agents.

---

### **1. Fully Observable vs. Partially Observable**

| **Type**                 | **Description**                                                                    |
| ------------------------ | ---------------------------------------------------------------------------------- |
| **Fully Observable**     | The agent's sensors can access the complete state of the environment at all times. |
| **Partially Observable** | The agent has only limited or noisy access to the environment’s state.             |

* **Example:**

  * Fully Observable: Chess (complete board visible)
  * Partially Observable: Driving in fog, poker (hidden cards)

---

### **2. Deterministic vs. Stochastic**

| **Type**          | **Description**                                                                                          |
| ----------------- | -------------------------------------------------------------------------------------------------------- |
| **Deterministic** | The next state of the environment is completely determined by the current state and the agent’s actions. |
| **Stochastic**    | The environment includes elements of randomness or uncertainty.                                          |

* **Example:**

  * Deterministic: Crossword puzzle
  * Stochastic: Stock market, card games

---

### **3. Episodic vs. Sequential**

| **Type**       | **Description**                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------ |
| **Episodic**   | The agent's experience is divided into atomic episodes; each decision is independent of previous ones. |
| **Sequential** | The current decision can affect all future decisions.                                                  |

* **Example:**

  * Episodic: Image classification
  * Sequential: Chess game, robot navigation

---

### **4. Static vs. Dynamic**

| **Type**    | **Description**                                                    |
| ----------- | ------------------------------------------------------------------ |
| **Static**  | The environment does not change while the agent is deliberating.   |
| **Dynamic** | The environment changes during decision-making or between actions. |

* **Example:**

  * Static: Turn-based games
  * Dynamic: Real-time systems, autonomous vehicles

---

### **5. Discrete vs. Continuous**

| **Type**       | **Description**                                           |
| -------------- | --------------------------------------------------------- |
| **Discrete**   | A limited number of clearly defined percepts and actions. |
| **Continuous** | The percepts and actions can take on a range of values.   |

* **Example:**

  * Discrete: Board games (like checkers)
  * Continuous: Robot arm control, real-world driving

---

### **6. Single-Agent vs. Multi-Agent**

| **Type**         | **Description**                                              |
| ---------------- | ------------------------------------------------------------ |
| **Single-Agent** | Only one agent is acting in the environment.                 |
| **Multi-Agent**  | Multiple agents exist, interacting or competing/cooperating. |

* **Example:**

  * Single-Agent: Sudoku solver
  * Multi-Agent: Soccer simulation, autonomous drone swarm

---

### **7. Observable Properties Summary Table**

| **Environment Property** | **Type 1**       | **Type 2**           | **Description**                                        |
| ------------------------ | ---------------- | -------------------- | ------------------------------------------------------ |
| Observability            | Fully Observable | Partially Observable | Can the agent see the full state?                      |
| Determinism              | Deterministic    | Stochastic           | Are outcomes predictable?                              |
| Episodicity              | Episodic         | Sequential           | Are actions independent or interdependent?             |
| Dynamics                 | Static           | Dynamic              | Does the environment change during decision making?    |
| Discreteness             | Discrete         | Continuous           | Is the number of states/actions finite or infinite?    |
| Agent Type               | Single-Agent     | Multi-Agent          | Are there other agents acting in the same environment? |

---

### **8. Real-World Example**

**Autonomous Car Environment:**

* **Partially Observable** (limited sensor range)
* **Stochastic** (uncertain traffic behavior)
* **Sequential** (previous actions affect future state)
* **Dynamic** (other vehicles and pedestrians are moving)
* **Continuous** (speed, position, steering angle)
* **Multi-Agent** (other cars, pedestrians, traffic systems)

---

### **9. Importance in AI System Design**

* Helps determine:

  * Suitable agent architecture (reflex, goal-based, utility-based)
  * Required algorithms (search, planning, learning)
  * Complexity of problem-solving
  * Degree of uncertainty handling needed

---
### **Structure of Agents**

---

An **agent** is an entity that **perceives** its environment through **sensors** and **acts** upon that environment through **actuators**. The **structure of an agent** defines how it is built internally to function effectively based on the percepts it receives.

---

### **1. Components of an Agent**

| **Component**        | **Description**                                                         |
| -------------------- | ----------------------------------------------------------------------- |
| **Sensors**          | Devices used to perceive the environment.                               |
| **Actuators**        | Devices used to act upon the environment.                               |
| **Percept**          | Input received at a given moment from the environment.                  |
| **Percept Sequence** | Entire history of all percepts received so far.                         |
| **Agent Program**    | Function that maps percepts to actions (implements the agent function). |
| **Agent Function**   | Abstract mathematical mapping from percept sequence to actions.         |

---

### **2. Agent Program**

* The **agent program** implements the agent function.
* It receives the **percept** from the environment and outputs an **action** based on logic, data, rules, or learning.
* This can be coded as rules, decision trees, machine learning models, etc.

---

### **3. Types of Agent Structures (Architectures)**

---

#### **a. Simple Reflex Agent**

| Feature            | Description                                                |
| ------------------ | ---------------------------------------------------------- |
| Decision Mechanism | Uses condition-action rules.                               |
| Internal State     | None (does not use percept history).                       |
| Behavior           | Reacts only to current percept.                            |
| Example            | Vacuum cleaner that moves left/right based on dirt sensor. |

**Structure:**

* If **condition** (percept) is true → take specific **action**.

---

#### **b. Model-Based Reflex Agent**

| Feature            | Description                                                          |
| ------------------ | -------------------------------------------------------------------- |
| Decision Mechanism | Uses condition-action rules **and internal state**.                  |
| Internal State     | Maintains a model of the environment.                                |
| Behavior           | Makes decisions even with partial observability.                     |
| Example            | Mobile robot navigating a building with memory of visited locations. |

**Structure:**

* Maintains internal model → updates model using new percept → uses model and rules to decide actions.

---

#### **c. Goal-Based Agent**

| Feature            | Description                                       |
| ------------------ | ------------------------------------------------- |
| Decision Mechanism | Uses search and planning to achieve goals.        |
| Internal State     | Maintains model of world and goal.                |
| Behavior           | Selects actions that achieve specified goals.     |
| Example            | Path-finding robot planning route to destination. |

**Structure:**

* Evaluate actions based on whether they help reach goal state.

---

#### **d. Utility-Based Agent**

| Feature            | Description                                                            |
| ------------------ | ---------------------------------------------------------------------- |
| Decision Mechanism | Chooses actions based on **utility function** (numerical preferences). |
| Internal State     | Maintains model of the world and utility estimates.                    |
| Behavior           | Selects action with the highest expected utility.                      |
| Example            | AI system choosing between risky and safe investment options.          |

**Structure:**

* Chooses action that **maximizes utility**, not just achieves goals.

---

#### **e. Learning Agent**

| Feature            | Description                                                                    |
| ------------------ | ------------------------------------------------------------------------------ |
| Decision Mechanism | Learns and improves from experience.                                           |
| Components         | Includes learning element, performance element, critic, and problem generator. |
| Behavior           | Adapts to new situations, improves over time.                                  |
| Example            | AI that learns to play a game better with each attempt.                        |

**Structure:**

* **Learning Element:** Improves agent performance.
* **Performance Element:** Chooses external actions.
* **Critic:** Provides feedback based on performance.
* **Problem Generator:** Suggests new experiences to learn from.

---

### **4. Summary Table of Agent Structures**

| **Agent Type**     | **Uses Internal State?** | **Uses Goals?** | **Uses Utility?** | **Learns?** |
| ------------------ | ------------------------ | --------------- | ----------------- | ----------- |
| Simple Reflex      | ❌                        | ❌               | ❌                 | ❌           |
| Model-Based Reflex | ✅                        | ❌               | ❌                 | ❌           |
| Goal-Based         | ✅                        | ✅               | ❌                 | ❌           |
| Utility-Based      | ✅                        | ✅               | ✅                 | ❌           |
| Learning Agent     | ✅                        | ✅               | ✅                 | ✅           |

---

### **5. Example: Autonomous Car**

| **Component** | **Example**                                       |
| ------------- | ------------------------------------------------- |
| Sensors       | Cameras, lidar, radar, GPS                        |
| Actuators     | Steering wheel, brakes, accelerator               |
| Percepts      | Lane markings, speed limits, obstacle positions   |
| Agent Program | Path planning, obstacle avoidance, decision logic |
| Goal          | Reach destination safely and efficiently          |
| Utility       | Minimize fuel, time, maximize safety and comfort  |
| Learning      | Improve driving strategy from past experiences    |

---
### **Solving Problems by Searching**

---

#### **1. Introduction**

* **Problem-solving by searching** is a fundamental approach in AI where an agent tries to find a sequence of actions leading from an initial state to a goal state.
* It involves exploring a **state space** representing all possible configurations or conditions of the problem.

---

#### **2. Problem-Solving Agent**

* A problem-solving agent formulates the problem from the current percept and uses search algorithms to find a solution path.
* The agent then executes the actions along this path.

---

#### **3. Problem Formulation**

* Defining a problem precisely is critical to apply search techniques.
* A problem is usually described by:

  1. **Initial State**

     * The state where the agent starts.
  2. **Actions (Successor Function)**

     * The set of possible actions the agent can perform.
     * Each action leads to a successor state.
  3. **Transition Model**

     * Describes the result of performing an action in a state.
  4. **Goal Test**

     * A function to determine if a given state is a goal state.
  5. **Path Cost**

     * A numeric cost associated with a path (often the sum of action costs).
     * The agent aims to minimize the path cost.

---

#### **4. State Space**

* The set of all states reachable from the initial state via actions.
* Can be represented as a **graph** or **tree** where nodes are states and edges are actions.

---

#### **5. Search Strategies**

---

##### **a. Uninformed (Blind) Search**

* Search strategies that use no information about the goal other than the problem definition.

* **Characteristics:**

  * Explore the search space blindly.
  * May be inefficient.

* **Examples:**

  * **Breadth-First Search (BFS)**

    * Explores all nodes at a given depth before moving deeper.
    * Guarantees finding the shortest path if all step costs are equal.
    * Uses a queue (FIFO) data structure.
  * **Depth-First Search (DFS)**

    * Explores as deep as possible along one branch before backtracking.
    * Uses a stack (LIFO) data structure.
    * May get stuck in infinite paths if cycles are present.
  * **Uniform-Cost Search**

    * Expands the node with the lowest path cost.
    * Uses a priority queue.
    * Finds optimal solutions when costs vary.

---

##### **b. Informed (Heuristic) Search**

* Uses problem-specific knowledge to guide the search.

* Evaluates nodes based on estimated cost to reach the goal.

* Typically more efficient than uninformed search.

* **Examples:**

  * **Hill Climbing**

    * Moves to neighbor states with better evaluation.
    * Can get stuck in local maxima, plateaus, or ridges.

  * **Best-First Search**

    * Expands nodes based on evaluation function $f(n)$.

  * **A\* Search**

    * Combines path cost $g(n)$ and heuristic estimate $h(n)$.
    * Evaluation function: $f(n) = g(n) + h(n)$.
    * Guarantees optimal solutions if $h(n)$ is admissible (never overestimates cost).

---

#### **6. Search Tree and Graph Search**

* **Tree Search:** May revisit states multiple times.
* **Graph Search:** Maintains a list of explored states to avoid revisiting.

---

#### **7. Components of a Search Problem**

| Component        | Description                                     |
| ---------------- | ----------------------------------------------- |
| Initial State    | Starting point of the search                    |
| Actions          | Set of possible moves from a state              |
| Transition Model | Function mapping state and action to new state  |
| Goal Test        | Checks if a state is the goal                   |
| Path Cost        | Cost function to evaluate the quality of a path |

---

#### **8. Performance Measures for Search Algorithms**

* **Completeness:** Will the algorithm find a solution if one exists?
* **Optimality:** Will the algorithm find the least-cost solution?
* **Time Complexity:** How much time does it take to find a solution?
* **Space Complexity:** How much memory is used during search?

---

#### **9. Example Problem: 8-Puzzle**

* **Initial State:** Tiles in some scrambled order.
* **Actions:** Move blank tile up, down, left, or right.
* **Goal Test:** Tiles arranged in order.
* **Path Cost:** Number of moves.
* Use BFS or A\* for solution search.

---

#### **10. Summary**

* Problem solving by searching involves defining the problem, generating a state space, and applying search strategies.
* Uninformed search explores blindly; informed search uses heuristics to guide exploration.
* Efficient problem-solving requires choosing appropriate search algorithms based on problem characteristics.

---
### **Problem-Solving Agents**

---

#### **1. Definition**

* A **problem-solving agent** is an AI agent designed to solve specific problems by finding a sequence of actions that lead from the current state to a goal state.
* It uses **search algorithms** to explore possible action sequences and select the best path to the goal.

---

#### **2. Working of a Problem-Solving Agent**

* The agent operates by:

  1. **Perceiving** the current state of the environment.
  2. **Formulating** the problem based on the current state.
  3. **Searching** for a solution (a sequence of actions) to reach the goal.
  4. **Executing** the found solution, action by action.
  5. If the environment changes or the plan fails, it reformulates and replans.

---

#### **3. Problem Formulation Components**

* **Initial State:** The state where the agent starts.
* **Actions:** Possible moves the agent can take.
* **Transition Model:** Resulting state after an action.
* **Goal Test:** A function to check if the current state satisfies the goal condition.
* **Path Cost:** Cost function to evaluate the total cost of the sequence of actions.

---

#### **4. Architecture of a Problem-Solving Agent**

| **Component**                 | **Description**                                          |
| ----------------------------- | -------------------------------------------------------- |
| **Percept Sequence**          | History of percepts received from environment            |
| **Problem Formulator**        | Creates a problem definition from percepts               |
| **Solver (Search Algorithm)** | Searches for a solution path in the state space          |
| **Plan Executor**             | Executes the sequence of actions generated by the solver |

---

#### **5. Algorithmic Steps**

1. **Perceive** current state from environment.
2. **Formulate** problem: define initial state, goal, actions.
3. **Search** for solution path using search strategies (BFS, DFS, A\*, etc.).
4. If solution found:

   * Extract the sequence of actions (plan).
   * Execute actions sequentially.
5. If plan fails or environment changes:

   * Reformulate problem.
   * Repeat search and execution.

---

#### **6. Characteristics**

* The agent is **goal-directed** and uses problem-solving methods.
* It can plan ahead before acting.
* It can handle deterministic and static environments effectively.
* Can be computationally expensive depending on search space size.

---

#### **7. Example**

**Vacuum Cleaner Agent:**

* **Initial State:** Current location and dirt status.
* **Actions:** Move left, move right, suck dirt.
* **Goal:** Clean all dirty squares.
* The agent perceives the current location, formulates the cleaning problem, searches for a sequence of moves to clean the environment, and executes them.

---

#### **8. Advantages**

* Provides a clear, structured approach to problem-solving.
* Allows use of powerful search algorithms.
* Can be generalized to many domains with proper problem formulation.

---

#### **9. Limitations**

* Performance depends on how well the problem is formulated.
* Large state spaces can cause combinatorial explosion.
* Not suitable for highly dynamic or partially observable environments without enhancements.

---

#### **10. Summary**

* Problem-solving agents apply search-based strategies to determine action sequences leading to goals.
* Their effectiveness relies on problem formulation, choice of search algorithms, and environment characteristics.

---
### **Formulating Problems**

---

Problem formulation is the process of defining a problem in a way that an AI agent can understand and solve it using search techniques. It involves specifying the key elements of the problem clearly and precisely.

---

### **1. Purpose of Problem Formulation**

* To translate a real-world task into a formal representation.
* To identify states, actions, and goals that enable the use of search algorithms.
* To enable systematic exploration of possible solutions.

---

### **2. Components of Problem Formulation**

| **Component**        | **Description**                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Initial State**    | The state from which the agent starts solving the problem.                                                         |
| **State Space**      | The set of all possible states reachable from the initial state via actions.                                       |
| **Actions**          | The possible operations or moves the agent can perform from a given state (successor function).                    |
| **Transition Model** | A description or function that defines the result of applying an action to a state (state → state).                |
| **Goal Test**        | A function to check if a given state satisfies the goal condition (true if goal reached).                          |
| **Path Cost**        | A numeric cost associated with moving from one state to another (used to evaluate the quality of a solution path). |

---

### **3. Example of Problem Formulation**

**8-Puzzle Problem:**

| Component        | Example Description                                                 |
| ---------------- | ------------------------------------------------------------------- |
| Initial State    | A particular arrangement of the tiles (scrambled).                  |
| State Space      | All possible arrangements of the tiles.                             |
| Actions          | Moving the blank tile up, down, left, or right.                     |
| Transition Model | Resulting configuration after moving the blank tile in a direction. |
| Goal Test        | Tiles arranged in the correct order (goal configuration).           |
| Path Cost        | Number of moves made to reach a state (each move costs 1).          |

---

### **4. Criteria for Effective Problem Formulation**

* **Well-defined states and actions:** Clear, unambiguous definitions.
* **Finite or manageable state space:** To make search computationally feasible.
* **Goal clarity:** Precise and testable goal conditions.
* **Meaningful cost function:** To prioritize optimal solutions.
* **Deterministic transition model:** Predictable outcomes of actions when possible.

---

### **5. Types of Problems**

* **Single-state problems:** The agent knows exactly which state it is in.
* **Multiple-state problems:** The agent has uncertainty about its current state.
* **Contingency problems:** Require planning for different contingencies.
* **Exploration problems:** Require discovering new states during problem-solving.

---

### **6. Representation**

* Problems are often represented as **state spaces** where nodes are states and edges represent actions.
* This representation facilitates the use of graph/tree search algorithms.

---

### **7. Summary**

* Problem formulation defines the problem environment for search algorithms.
* It identifies initial states, goals, actions, and costs.
* Proper formulation is essential for effective problem solving and efficient search.

---
### **Example Problems in Artificial Intelligence Problem Solving**

---

#### **1. Vacuum Cleaner World**

* **Description:**
  A simple environment where a vacuum cleaner agent moves between two locations (A and B) and cleans dirt.

* **Problem Components:**

  * **Initial State:** Vacuum at location A or B, locations may be clean or dirty.
  * **Actions:** Move left, move right, suck dirt.
  * **Goal:** Both locations are clean.
  * **Path Cost:** Number of actions taken.

---

#### **2. 8-Puzzle Problem**

* **Description:**
  A sliding puzzle with 8 numbered tiles and one blank space in a 3x3 grid. The goal is to arrange the tiles in order.

* **Problem Components:**

  * **Initial State:** Any scrambled arrangement of tiles.
  * **Actions:** Move the blank tile up, down, left, or right.
  * **Goal Test:** Tiles arranged in order from 1 to 8, blank in the last position.
  * **Path Cost:** Number of moves.

---

#### **3. Missionaries and Cannibals Problem**

* **Description:**
  Three missionaries and three cannibals need to cross a river with a boat. The boat can carry up to two people. The constraint is missionaries cannot be outnumbered by cannibals on either bank.

* **Problem Components:**

  * **Initial State:** All missionaries and cannibals on the left bank.
  * **Actions:** Move one or two people in the boat to the opposite bank.
  * **Goal:** All missionaries and cannibals safely on the right bank.
  * **Constraints:** Missionaries never outnumbered.
  * **Path Cost:** Number of crossings.

---

#### **4. Robot Navigation Problem**

* **Description:**
  A robot in a grid world must move from a start cell to a goal cell avoiding obstacles.

* **Problem Components:**

  * **Initial State:** Robot’s start position.
  * **Actions:** Move north, south, east, west (if no obstacle).
  * **Goal Test:** Robot reaches goal cell.
  * **Path Cost:** Distance traveled or number of moves.

---

#### **5. Traveling Salesman Problem (TSP)**

* **Description:**
  Find the shortest possible route that visits each city once and returns to the origin city.

* **Problem Components:**

  * **Initial State:** Starting city.
  * **Actions:** Travel to another unvisited city.
  * **Goal:** All cities visited and return to start.
  * **Path Cost:** Total distance traveled.

---

#### **6. Tic-Tac-Toe Game**

* **Description:**
  Two players alternate placing marks on a 3x3 grid aiming to get three in a row.

* **Problem Components:**

  * **Initial State:** Empty board.
  * **Actions:** Place mark (X or O) in an empty cell.
  * **Goal Test:** Three marks in a row or full board.
  * **Path Cost:** Number of moves (usually ignored).

---

#### **7. Maze Solving Problem**

* **Description:**
  Find a path from start to goal in a maze.

* **Problem Components:**

  * **Initial State:** Maze entrance position.
  * **Actions:** Move up, down, left, right (if not blocked).
  * **Goal:** Reach maze exit.
  * **Path Cost:** Number of moves or steps.

---

### **Summary**

* These problems vary in complexity, environment type, and goals.
* They demonstrate different problem-solving scenarios where AI search techniques apply.
* Understanding these examples aids in grasping problem formulation and search strategies.

### **Searching for Solutions**

---

Searching for solutions involves systematically exploring the state space defined by a problem to find a sequence of actions that lead from the initial state to a goal state.

---

### **1. Search Space and Search Tree**

* **Search Space:**
  The set of all possible states reachable from the initial state by applying available actions.

* **Search Tree:**
  A tree structure where:

  * Nodes represent states.
  * Edges represent actions leading to successor states.
  * The root is the initial state.

---

### **2. Search Process**

* **Step 1: Initialize** with the initial state as the root node.
* **Step 2: Expand** nodes by generating their successor states via available actions.
* **Step 3: Check** if a newly generated state satisfies the goal test.
* **Step 4: If goal reached,** return the path (sequence of actions) from the root to this state.
* **Step 5: If not,** continue expanding nodes until goal found or all nodes explored.

---

### **3. Search Strategies**

* Search algorithms differ in **node expansion order**, **memory usage**, and **optimality**.
* Two main categories:

  * **Uninformed (Blind) Search:** No additional information about goal location.
  * **Informed (Heuristic) Search:** Uses domain knowledge or heuristics to guide the search.

---

### **4. Path to Solution**

* The solution is a **path** from the initial state to a goal state.
* The path consists of the sequence of actions chosen at each step.

---

### **5. Tree vs. Graph Search**

* **Tree Search:**

  * Expands nodes without remembering visited states.
  * May revisit states multiple times, possibly leading to inefficiency or infinite loops.

* **Graph Search:**

  * Keeps track of visited (explored) states to avoid repeated work.
  * More efficient and avoids cycles.

---

### **6. Handling Search Complexity**

* **Breadth and Depth Limits:** To prevent infinite searches.
* **Cost Functions:** To prioritize paths with lower cost.
* **Heuristics:** To estimate distance to goal and guide expansion.

---

### **7. Example: Searching in 8-Puzzle**

* Initial scrambled state is root.
* Expand by moving blank tile in possible directions.
* Use search algorithm to find path to ordered goal state.
* Extract solution path (move sequences) once goal found.

---

### **8. Summary**

* Searching for solutions systematically explores the problem’s state space.
* Success depends on search strategy and problem structure.
* Efficient search balances exploration and exploitation to find optimal or satisfactory solutions.

---

### **Uninformed Search Strategies**

Uninformed search strategies, also known as blind search, explore the search space without any knowledge about the goal’s location other than the problem definition. They systematically examine states but do not use any heuristic information to guide the search.

---

### **1. Characteristics of Uninformed Search**

* No domain-specific knowledge or heuristics.
* Only use information available in the problem definition.
* Explore the search space blindly.
* May be inefficient in large or complex problems.

---

### **2. Common Uninformed Search Strategies**

---

#### **a. Breadth-First Search (BFS)**

* **Approach:** Explores all nodes at a given depth before moving to the next depth level.
* **Data Structure:** Uses a **FIFO queue**.
* **Properties:**

  * Complete (will find a solution if one exists).
  * Optimal if all step costs are equal.
  * Time Complexity: $O(b^d)$, where $b$ is branching factor, $d$ is depth of shallowest solution.
  * Space Complexity: $O(b^d)$ (stores all nodes at current depth).
* **Use Case:** Problems with small depth or equal step costs.

---

#### **b. Depth-First Search (DFS)**

* **Approach:** Explores as deep as possible along a branch before backtracking.
* **Data Structure:** Uses a **stack** or recursion.
* **Properties:**

  * Not complete in infinite-depth spaces or spaces with loops.
  * Not optimal.
  * Time Complexity: $O(b^m)$, where $m$ is maximum depth of search tree.
  * Space Complexity: $O(bm)$ (stores only nodes along current path).
* **Use Case:** When memory is limited and solutions are deep.

---

#### **c. Depth-Limited Search**

* **Approach:** DFS with a predetermined depth limit $l$.
* **Properties:**

  * Complete if solution depth ≤ limit.
  * Not complete if solution depth > limit.
  * Prevents infinite search in cyclic or infinite spaces.
* **Use Case:** When the maximum depth of solution is known or bounded.

---

#### **d. Iterative Deepening Depth-First Search (IDDFS)**

* **Approach:** Repeatedly applies depth-limited search with increasing depth limits (0, 1, 2, …).
* **Properties:**

  * Complete like BFS.
  * Optimal like BFS if step costs are equal.
  * Time Complexity: $O(b^d)$.
  * Space Complexity: $O(bd)$.
* **Use Case:** Combines benefits of BFS (completeness) and DFS (low memory).

---

#### **e. Uniform-Cost Search (UCS)**

* **Approach:** Expands the node with the lowest cumulative path cost $g(n)$.
* **Data Structure:** Priority queue ordered by path cost.
* **Properties:**

  * Complete if step costs ≥ some positive constant.
  * Optimal: Finds least-cost solution.
  * Time and space complexity depend on path costs.
* **Use Case:** Problems with varying step costs where optimality matters.

---

### **3. Summary Table**

| Search Strategy                 | Complete | Optimal                   | Time Complexity  | Space Complexity | Remarks                                            |
| ------------------------------- | -------- | ------------------------- | ---------------- | ---------------- | -------------------------------------------------- |
| Breadth-First Search (BFS)      | Yes      | Yes (if step costs equal) | $O(b^d)$         | $O(b^d)$         | Memory-intensive                                   |
| Depth-First Search (DFS)        | No       | No                        | $O(b^m)$         | $O(bm)$          | May get stuck in infinite depth                    |
| Depth-Limited Search            | No       | No                        | $O(b^l)$         | $O(bl)$          | Depends on depth limit                             |
| Iterative Deepening DFS (IDDFS) | Yes      | Yes                       | $O(b^d)$         | $O(bd)$          | Combines BFS completeness and DFS space efficiency |
| Uniform-Cost Search (UCS)       | Yes      | Yes                       | Depends on costs | Depends on costs | Optimal for varying costs                          |

---

### **4. Application Considerations**

* **BFS** preferred when solution is shallow and step costs equal.
* **DFS** preferred when memory is limited, solution depth unknown.
* **IDDFS** preferred for large or infinite state spaces.
* **UCS** preferred when costs vary and optimality is important.

---

### **5. Limitations**

* Inefficient for large or complex problems without heuristics.
* Memory usage can be prohibitive for BFS and UCS.

---

### **Breadth-First Search (BFS)**

---

#### **1. Definition**

* BFS is an **uninformed search algorithm** that explores the search space level by level.
* It expands all nodes at a given depth before moving to the next deeper level.
* BFS uses a **first-in, first-out (FIFO) queue** to manage the frontier.

---

#### **2. Working Principle**

* Start at the **initial state** and add it to the queue.
* Repeat the following until the queue is empty or the goal is found:

  1. Remove the first node from the queue (the oldest node).
  2. Check if the node is the **goal state**; if yes, return the solution.
  3. Otherwise, expand the node by generating all its successor states.
  4. Add all unvisited successors to the end of the queue.

---

#### **3. Key Properties**

| Property             | Description                                                                          |
| -------------------- | ------------------------------------------------------------------------------------ |
| **Completeness**     | Yes, BFS will find a solution if one exists (finite state space).                    |
| **Optimality**       | Yes, if all step costs are equal (finds the shortest path).                          |
| **Time Complexity**  | $O(b^d)$, where $b$ is branching factor and $d$ is depth of the shallowest solution. |
| **Space Complexity** | $O(b^d)$, stores all nodes at the current depth level.                               |

---

#### **4. Data Structures Used**

* **Queue (FIFO):**
  Stores nodes in the order they are generated to ensure level-order expansion.

* **Explored Set:**
  To avoid revisiting the same states multiple times (if implemented).

---

#### **5. Advantages**

* Guarantees the shortest path solution in uniform cost problems.
* Simple to implement.
* Systematic and complete in finite spaces.

---

#### **6. Disadvantages**

* Requires large memory because it stores all nodes at a given depth.
* Can be slow for problems with large branching factors or deep solutions.

---

#### **7. Example**

* **Problem:** Finding the shortest path in a maze from start to goal.
* BFS explores all positions reachable in 1 step, then all in 2 steps, and so forth until it finds the goal.

---

#### **8. Pseudocode**

```python
BFS(problem):
    initialize queue with initial_state
    initialize explored set as empty
    while queue not empty:
        node = queue.dequeue()
        if problem.goal_test(node.state):
            return solution_path(node)
        explored.add(node.state)
        for each action in problem.actions(node.state):
            child = child_node(node, action)
            if child.state not in explored and child not in queue:
                queue.enqueue(child)
    return failure
```

---

#### **9. Summary**

* BFS is an uninformed search exploring nodes by increasing depth.
* It guarantees to find the shortest path if step costs are uniform.
* Memory-intensive due to wide frontiers at deeper levels.

---
### **Depth-First Search (DFS)**

---

#### **1. Definition**

* DFS is an **uninformed search algorithm** that explores as far as possible along each branch before backtracking.
* It goes deep into the search tree by expanding the most recently generated node first.
* DFS uses a **stack** (either explicitly or via recursion) to manage nodes.

---

#### **2. Working Principle**

* Start at the **initial state**.
* Explore a branch by moving down to a successor until reaching a **goal state** or a **dead end**.
* If dead end or no more successors, backtrack to the most recent node with unexplored successors.
* Continue until the goal is found or all nodes are explored.

---

#### **3. Key Properties**

| Property             | Description                                                                   |
| -------------------- | ----------------------------------------------------------------------------- |
| **Completeness**     | No, DFS may get stuck in infinite-depth spaces or loops.                      |
| **Optimality**       | No, DFS does not guarantee shortest path or least cost solution.              |
| **Time Complexity**  | $O(b^m)$, where $b$ is branching factor and $m$ is maximum depth of the tree. |
| **Space Complexity** | $O(bm)$, stores nodes along the current path only.                            |

---

#### **4. Data Structures Used**

* **Stack (LIFO):**
  Stores nodes to explore, with last generated node explored first.
* Can be implemented via recursion call stack.

---

#### **5. Advantages**

* Uses much less memory than BFS.
* Can find a solution without storing all nodes.
* Simple and easy to implement recursively.

---

#### **6. Disadvantages**

* May not find a solution if it goes into infinite depth or loops.
* Not optimal: may find longer paths.
* Can get stuck in deep or infinite branches without depth limits.

---

#### **7. Example**

* **Problem:** Navigating a maze.
* DFS explores one path deeply before trying alternative paths.
* May find a solution quickly but not necessarily the shortest.

---

#### **8. Pseudocode**

```python
DFS(problem):
    initialize stack with initial_state
    initialize explored set as empty
    while stack not empty:
        node = stack.pop()
        if problem.goal_test(node.state):
            return solution_path(node)
        explored.add(node.state)
        for each action in problem.actions(node.state):
            child = child_node(node, action)
            if child.state not in explored and child not in stack:
                stack.push(child)
    return failure
```

---

#### **9. Summary**

* DFS explores deeply down branches before backtracking.
* Efficient in memory but can be incomplete or inefficient in some problems.
* Not guaranteed to find the shortest or least cost path.

---
### **Breadth-First Search (BFS) vs Depth-First Search (DFS)**

| Feature                       | Breadth-First Search (BFS)                                                  | Depth-First Search (DFS)                                                |
| ----------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Search Strategy**           | Explores nodes level by level (layer-wise)                                  | Explores as deep as possible along each branch first                    |
| **Data Structure Used**       | Queue (FIFO)                                                                | Stack (LIFO) or recursion                                               |
| **Completeness**              | Complete (will find a solution if one exists in finite space)               | Not complete (may get stuck in infinite loops or deep paths)            |
| **Optimality**                | Optimal if all step costs are equal (finds shortest path)                   | Not optimal (may find a non-shortest path)                              |
| **Time Complexity**           | $O(b^d)$ (where $b$ = branching factor, $d$ = depth of shallowest solution) | $O(b^m)$ (where $m$ = maximum depth of the search tree)                 |
| **Space Complexity**          | $O(b^d)$ (stores all nodes at current depth level)                          | $O(bm)$ (stores only nodes along current path)                          |
| **Memory Usage**              | High memory consumption (stores all nodes at current depth)                 | Low memory consumption (stores current path only)                       |
| **Usage Scenario**            | Suitable when shallow solutions are expected or shortest path is required   | Suitable for problems with large state spaces or when memory is limited |
| **Risk of Infinite Loops**    | Avoided if implemented with explored set                                    | High risk unless depth limit or cycle detection used                    |
| **Implementation Complexity** | Simple with queue                                                           | Simple with recursion or stack                                          |
| **When to Use**               | When solution depth is small or unknown but optimality is important         | When solution depth is large, or space is limited                       |

---

### **Summary**

* BFS systematically explores all nodes at a given depth before going deeper, guaranteeing shortest path but with high memory use.
* DFS explores deep down a path quickly, using less memory but risking getting stuck in deep or infinite paths and not guaranteeing shortest solutions.

### **Search with Partial Information**

---

Search with partial information deals with problem-solving when the agent does **not have complete or perfect knowledge** of the environment’s current state. Unlike classical search, where the agent knows the exact state, here the agent must act under **uncertainty** or **incomplete percepts**.

---

### **1. Characteristics of Partial Information Search**

* The agent’s **percept** does not fully specify the current state.
* The agent must maintain a **belief state** (a set or probability distribution over possible actual states).
* The search space is over these **belief states** rather than concrete states.
* Often involves **probabilistic** or **non-deterministic** models.

---

### **2. Belief State**

* Represents all possible states the environment might be in, given the agent’s observations so far.
* The agent updates the belief state as it receives new percepts.

---

### **3. Approaches to Searching with Partial Information**

---

#### **a. Contingency Planning**

* Plans that specify actions based on possible observations or outcomes.
* Includes branches for different contingencies (if-then-else).
* Creates conditional plans to handle uncertainty.

---

#### **b. Sensor-Based Planning**

* Integrates sensory inputs during execution.
* The plan adapts dynamically as new information is acquired.

---

#### **c. Probabilistic Search**

* Uses probabilities to represent uncertainty in state.
* Employs algorithms like **Partially Observable Markov Decision Processes (POMDPs)**.
* Optimizes expected utility over uncertain states.

---

### **4. Example Problems**

* **Robot localization:** Robot does not know its exact position but infers location based on sensor readings.
* **Navigation in unknown terrain:** The agent explores while building a map.
* **Card games:** Players have incomplete knowledge of opponents’ cards.

---

### **5. Search Algorithms Handling Partial Information**

| Algorithm/Technique     | Description                                                                                                 |
| ----------------------- | ----------------------------------------------------------------------------------------------------------- |
| **AND-OR Search Trees** | Plans for all contingencies, with AND nodes for all possible outcomes and OR nodes for alternative actions. |
| **Belief State Search** | Searches in the space of belief states rather than concrete states.                                         |
| **POMDP Solvers**       | Use probabilistic models to choose actions under uncertainty.                                               |

---

### **6. Challenges**

* The belief state space is often exponentially larger than concrete states.
* Planning under uncertainty requires more computation.
* Requires balance between exploration and exploitation.

---

### **7. Summary**

* Search with partial information handles uncertainty by maintaining and reasoning over possible states.
* Solutions often involve contingency or probabilistic planning.
* Widely applicable in real-world problems where complete knowledge is unavailable.

---
### **Heuristic Search**

---

#### **1. Definition**

* Heuristic search is a search strategy that uses **problem-specific knowledge** (heuristics) to **guide** the search process towards the goal more efficiently than uninformed methods.
* A **heuristic function** estimates how close a given state is to the goal, helping prioritize which nodes to explore first.

---

#### **2. Purpose**

* To improve search efficiency by reducing the number of nodes expanded.
* To find solutions faster in large or complex state spaces.

---

#### **3. Key Concepts**

| Term                                 | Description                                                                                         |
| ------------------------------------ | --------------------------------------------------------------------------------------------------- |
| **Heuristic Function $h(n)$**        | Estimates the cost from node $n$ to the goal. Must be computationally cheap to evaluate.            |
| **Evaluation Function $f(n)$**       | Combines path cost and heuristic estimate, e.g., $f(n) = g(n) + h(n)$ in A\*.                       |
| **Admissible Heuristic**             | Never overestimates the true cost to reach the goal (optimistic). Ensures optimality in A\*.        |
| **Consistent (Monotonic) Heuristic** | Satisfies triangle inequality: $h(n) \leq c(n,a,n') + h(n')$. Guarantees optimality and efficiency. |

---

#### **4. Common Heuristic Search Algorithms**

---

##### **a. Hill Climbing**

* Moves iteratively to the neighbor state with the best heuristic value.
* Stops when no neighbor improves the heuristic.
* Prone to local maxima, plateaus, or ridges.

---

##### **b. Best-First Search**

* Expands nodes based solely on heuristic $h(n)$.
* Greedy, focuses on estimated closeness to goal.
* Not guaranteed to find optimal solutions.

---

##### **c. A* Search*\*

* Uses evaluation function $f(n) = g(n) + h(n)$, where:

  * $g(n)$ = cost so far to reach node $n$.
  * $h(n)$ = estimated cost from $n$ to goal.
* Explores paths that appear cheapest considering both cost so far and estimated cost remaining.
* Guaranteed to find the optimal path if $h(n)$ is admissible and consistent.

---

#### **5. Advantages of Heuristic Search**

* More efficient than uninformed search in large state spaces.
* Focuses exploration on promising paths.
* Can handle complex problems like puzzles, route planning, game playing.

---

#### **6. Example**

* **8-Puzzle Problem:**

  * Heuristic $h(n)$ could be the number of misplaced tiles or Manhattan distance of tiles from their goal positions.
  * A\* uses these heuristics to find the shortest sequence of moves.

---

#### **7. Summary**

* Heuristic search leverages domain knowledge via heuristics to guide search.
* Balances between exploration (cost so far) and exploitation (estimated cost to goal).
* Algorithms like A\* combine heuristics with path cost to guarantee optimal and efficient search.

---
### **Hill Climbing**

---

#### **1. Definition**

* Hill climbing is a **heuristic search algorithm** that continuously moves in the direction of increasing (or decreasing) value of a heuristic evaluation function.
* It is a form of **local search** aiming to find a peak (maximum) or valley (minimum) in the search space.

---

#### **2. Working Principle**

* Start from an initial state.
* Evaluate neighboring states.
* Move to the neighbor with the best improvement in the heuristic value.
* Repeat until no neighbor has a better value (local maximum/minimum reached).

---

#### **3. Algorithm Steps**

1. Initialize current state $s$ to initial state.
2. Loop:

   * Evaluate neighbors of $s$.
   * Select neighbor $s'$ with the best heuristic value better than $s$.
   * If no better neighbor, **stop** (local optimum).
   * Else, set $s = s'$.
3. Return current state $s$ as solution.

---

#### **4. Types of Hill Climbing**

| Type                              | Description                                           |
| --------------------------------- | ----------------------------------------------------- |
| **Simple Hill Climbing**          | Picks the first neighbor better than current state.   |
| **Steepest-Ascent Hill Climbing** | Evaluates all neighbors and chooses the best one.     |
| **Stochastic Hill Climbing**      | Randomly picks a better neighbor instead of the best. |

---

#### **5. Advantages**

* Simple to implement.
* Uses less memory (only current state and neighbors).
* Efficient for problems with smooth landscapes.

---

#### **6. Disadvantages / Limitations**

* **Local maxima:** Algorithm can get stuck on suboptimal peaks.
* **Plateaus:** Flat areas with no better neighbors cause search to stall.
* **Ridges:** Narrow peaks may be difficult to climb.
* No guarantee of finding the global optimum.

---

#### **7. Example**

* In the **8-puzzle**, hill climbing may choose moves that reduce the number of misplaced tiles.
* However, it can get stuck if no neighboring move improves the heuristic even if the goal is not reached.

---

#### **8. Applications**

* Optimization problems.
* Machine learning parameter tuning.
* Robotics path planning.
* Game playing with heuristic evaluations.

---

#### **9. Summary**

* Hill climbing is a local, greedy search strategy moving to better neighboring states.
* It is simple but prone to getting stuck in local optima.
* Useful when problem landscape is well-behaved or combined with methods to escape local maxima.

---
### **Best-First Search**

---

#### **1. Definition**

* Best-First Search is a **heuristic search algorithm** that selects which node to expand based on an evaluation function, typically estimating how close a node is to the goal.
* It expands the most promising node first, guided by a heuristic.

---

#### **2. Working Principle**

* Maintains a **priority queue (open list)** ordered by evaluation function $f(n)$.
* At each step:

  1. Remove the node with the best (lowest) evaluation score.
  2. Check if it is the goal state; if yes, return the solution.
  3. Otherwise, expand the node by generating successors.
  4. Insert successors into the priority queue with their evaluation scores.
* Repeat until goal is found or queue is empty.

---

#### **3. Evaluation Function**

* Commonly $f(n) = h(n)$, where $h(n)$ is a heuristic estimating cost to goal.
* Unlike A\*, it may not consider cost so far $g(n)$, focusing only on estimated remaining cost.

---

#### **4. Properties**

| Property             | Description                                                        |
| -------------------- | ------------------------------------------------------------------ |
| **Completeness**     | Not guaranteed (can get stuck in loops or infinite paths).         |
| **Optimality**       | Not guaranteed (does not necessarily find least-cost path).        |
| **Time Complexity**  | Depends on quality of heuristic; can be exponential in worst case. |
| **Space Complexity** | Can be high; stores all generated nodes in memory.                 |

---

#### **5. Differences from A\***

* Best-First Search uses only heuristic $h(n)$ to evaluate nodes.
* A\* Search uses $f(n) = g(n) + h(n)$ combining path cost and heuristic.
* A\* guarantees optimality (with admissible heuristics); Best-First does not.

---

#### **6. Advantages**

* Focuses search towards promising regions.
* Can be faster than uninformed search if heuristic is good.

---

#### **7. Disadvantages**

* May explore nodes that look promising but lead to dead ends.
* Vulnerable to loops without proper handling.
* Does not guarantee optimal solutions.

---

#### **8. Example**

* Searching for a path on a map using straight-line distance as heuristic $h(n)$.
* Best-First Search prioritizes nodes closest (by heuristic) to goal, but may ignore longer paths with lower actual cost.

---

#### **9. Summary**

* Best-First Search is a heuristic-guided search that prioritizes nodes estimated closest to the goal.
* Faster than uninformed search but lacks guarantees of completeness or optimality.
* Often used as a basis or component in other search algorithms like A\*.

---
### **A* Search Algorithm*\*

---

#### **1. Definition**

* A\* is a **heuristic search algorithm** that finds the least-cost path from the initial state to a goal state.
* It combines the actual cost to reach a node and an estimated cost to the goal, balancing exploration and exploitation.

---

#### **2. Evaluation Function**

* Uses the function:

  $$
  f(n) = g(n) + h(n)
  $$

  where:

  * $g(n)$ = cost from the start node to current node $n$.
  * $h(n)$ = heuristic estimate of cost from $n$ to goal.

---

#### **3. Working Principle**

* Initialize the **open list** (priority queue) with the initial node.
* Repeat:

  1. Remove the node $n$ from the open list with the lowest $f(n)$.
  2. If $n$ is the goal, reconstruct and return the path.
  3. Otherwise, expand $n$ to generate successors.
  4. For each successor $s$:

     * Calculate $g(s) = g(n) + c(n, s)$, where $c(n, s)$ is cost from $n$ to $s$.
     * Calculate $f(s) = g(s) + h(s)$.
     * If $s$ is not in open or closed lists or has a lower $g(s)$, update and add $s$ to open list.
  5. Add $n$ to the closed list (explored nodes).

---

#### **4. Properties**

| Property             | Description                                                               |
| -------------------- | ------------------------------------------------------------------------- |
| **Completeness**     | Complete if step costs > 0 and finite branching factor.                   |
| **Optimality**       | Optimal if heuristic $h(n)$ is **admissible** (never overestimates cost). |
| **Time Complexity**  | Exponential in worst case but efficient with good heuristics.             |
| **Space Complexity** | Stores all generated nodes; can be high.                                  |

---

#### **5. Heuristic Requirements**

* **Admissible:**
  $h(n) \leq$ true cost from $n$ to goal (never overestimates).
* **Consistent (Monotonic):**
  $h(n) \leq c(n, a, n') + h(n')$ for every action $a$ from $n$ to $n'$.
* Consistency implies admissibility and ensures optimal efficiency.

---

#### **6. Advantages**

* Guarantees to find an optimal solution if heuristic is admissible.
* More efficient than uninformed or pure heuristic searches.
* Flexible by choosing different heuristics for different problems.

---

#### **7. Disadvantages**

* Can consume large memory due to storing open and closed lists.
* Performance depends heavily on quality of heuristic.
* May be slow for very large or complex search spaces.

---

#### **8. Example**

* In the **8-puzzle problem**, using Manhattan distance as $h(n)$ allows A\* to find the shortest sequence of moves efficiently.

---

#### **9. Summary**

* A\* combines actual cost and heuristic estimates for informed, optimal search.
* It balances exploration and exploitation to find least-cost solutions.
* Widely used in AI, robotics, pathfinding, and game algorithms.

---
### **Hill Climbing vs Best-First Search vs A\***

| Feature                   | Hill Climbing                                        | Best-First Search                                      | A\* Search                                                |
| ------------------------- | ---------------------------------------------------- | ------------------------------------------------------ | --------------------------------------------------------- |
| **Search Type**           | Local search (greedy, moves to best neighbor)        | Heuristic search (uses heuristic only)                 | Heuristic search (uses cost + heuristic)                  |
| **Evaluation Function**   | Heuristic value $h(n)$ of current node's neighbors   | Heuristic $h(n)$ only                                  | $f(n) = g(n) + h(n)$ (cost so far + heuristic)            |
| **Search Scope**          | Explores neighbors of current node only              | Explores all frontier nodes                            | Explores all frontier nodes                               |
| **Memory Usage**          | Low (stores only current state and neighbors)        | Higher (stores open list of frontier nodes)            | Higher (stores open and closed lists)                     |
| **Completeness**          | No (can get stuck at local maxima or plateaus)       | No (may not find solution if loops or poor heuristic)  | Yes (if heuristic is admissible and consistent)           |
| **Optimality**            | No (greedy, may find suboptimal solutions)           | No (does not consider path cost)                       | Yes (with admissible heuristic)                           |
| **Handling Local Maxima** | Prone to getting stuck without additional techniques | Less prone than hill climbing, but can still get stuck | Avoids local maxima with consistent heuristic             |
| **Use Case**              | Quick approximation, optimization problems           | Fast heuristic-driven search, non-optimal paths        | Optimal pathfinding, balanced heuristic and cost          |
| **Speed**                 | Fast, but can stop prematurely                       | Faster than uninformed, depends on heuristic           | Efficient with good heuristics, slower than hill climbing |
| **Example Applications**  | Parameter tuning, optimization                       | Route finding with heuristic                           | Pathfinding in maps, game AI                              |

---

### **Summary**

* **Hill Climbing:** Simple, memory-efficient local search that moves greedily to better neighbors; not guaranteed to find global optimum or solution.
* **Best-First Search:** Uses heuristic to guide search over the whole frontier, faster than uninformed but may not find optimal solutions or guarantee completeness.
* **A\* Search:** Combines path cost and heuristic, guaranteeing optimal and complete solutions with admissible heuristics; more memory and computation intensive.


