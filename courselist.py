import sqlite3

connection = sqlite3.connect('courselist.db')
cursor = connection.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS schedules (
#                 schedule_id text,
#                 course1 text,
#                 course2 text,
#                 course3 text,
#                 course4 text);""")

# schedules = [
#     ('1', 'CS172', 'ENGL1110G', 'MATH1511G', 'Lab Science'),
#     ('2', 'CS271', 'CS273', 'MATH1511G', 'Lab Science'),
#     ('3', 'CS271', 'CS273', 'MATH1521G', 'Lab Science'),
#     ('4', 'CS272', 'CS278', 'COMM1115G', 'ENGL2210G'),
#     ('5', 'CS272', 'CS370', 'COMM1115G', 'ENGL2210G'),
#     ('6', 'CS278', 'CS370', 'COMM1115G', 'ENGL2210G'),
#     ('7', 'CS278', 'CS371', 'COMM1115G', 'AST311'),
#     ('8', 'CS278', 'CS371', 'MATH2415', 'AST311')
# ]
    
# cursor.execute("""CREATE TABLE IF NOT EXISTS course_list (
#                 id text, 
#                 name text, 
#                 credits integer, 
#                 description text, 
#                 prereq text, 
#                 sem_offered text);""")

# course_list = [
#     ('CS111', 'Computer Science Principles', 4, 'This course provides a broad and exciting introduction to the field of computer science and the impact that computation has today on every aspect of life. It focuses on exploring computing as a creative activity and investigates the key foundations of computing: abstraction, data, algorithms, and programming. It looks into how connectivity and the Internet have revolutionized computing and demonstrates the global impact that computing has achieved, and it reveals how a new student in computer science might become part of the computing future.', 'MATH1215', 'FA23, SP24, FA24, SP25'),
#     ('CS172', 'Computer Science I', 4, 'Computational problem solving; problem analysis; implementation of algorithms using Java. Object-oriented concepts, arrays, searching, sorting, and recursion.', 'MATH 1250G', 'FA23, SP24, FA24, SP25'),
#     ('CS271', 'Object Oriented Programming', 4, 'Introduction to problem analysis and problem solving in the object-oriented paradigm. Practical introduction to implementing solutions in the C++ language. Pointers and dynamic memory allocation. Hands-on experience with useful development tools.', 'CS172', 'FA23, SP24, FA24, SP25'),
#     ('CS272', 'Introduction to Data Structures', 4, 'Design, implementation, use of fundamental abstract data types and their algorithms: lists, stacks, queues, deques, trees; imperative and declarative programming. Internal sorting; time and space efficiency of algorithms.', 'CS172', 'FA23, SP24, FA24, SP25'),
#     ('CS273', 'Machine Programming and Organization', 4, 'Computer structure, instruction execution, addressing techniques; programming in machine and assembly languages.', 'CS172', 'FA23, SP24, FA24, SP25'),
#     ('CS278', 'Discrete Mathematics for Computer Science', 4, 'Discrete mathematics required for Computer Science, including the basics of logic, number theory, methods of proof, sequences, mathematical induction, set theory, counting, and functions.', 'CS172', 'FA23, SP24, FA24, SP25'),
#     ('CS343', 'Algorithm Design and Implementation', 3, 'Introduction to efficient data structure and algorithm design. Basic graph algorithms. Balanced search trees. Classic algorithm design paradigms: divide-and-conquer, greedy scheme, and dynamic programming.', 'CS272', 'SP24, SP25'),
#     ('CS370', 'Compilers and Automata Theory', 4, 'Methods, principles, and tools for programming language processor design; basics of formal language theory (finite automata, regular expressions, context-free grammars); development of compiler components.', 'CS271, CS272, CS273', 'FA23, SP24, FA24, SP25'),
#     ('CS371', 'Software Development', 4, 'Software specification, design, testing, maintenance, documentation; informal proof methods; team implementation of a large project.', 'CS271, CS272', 'FA23, SP24, FA24, SP25'),
#     ('CS372', 'Data Structures and Algorithms', 4, 'Introduction to efficient data structure and algorithm design. Order notation and asymptotic run-time of algorithms. Recurrence relations and solutions. Abstract data type dynamic set and red-black trees. Classic algorithm design paradigms: divide-and-conquer, dynamic programming, greedy algorithms.', 'CS272, CS278', 'FA23, SP24, FA24, SP25'),
#     ('CS380', 'Introduction to Cryptography', 3, 'The course covers basic cryptographic primitives, such as symmetric, public-key ciphers, digital signature schemes, and hash functions, and their mathematical underpinnings. Course helps students understand basic notions of security in a cryptographic sense: chosen plaintext and chosen ciphertext attacks, games, and reductions. Course also covers computational number theory relevant to cryptography. Consent of Instructor required.', 'CS278', 'FA23, FA24'),
#     ('CS382', 'Modern Web Technologies', 3, 'In this course, we will take a full-stack approach to modern web application design. We will start with the fundamentals including HTML5, CSS3, Javascript, JSON, and the underlying networking concepts and protocols driving the modern web. We will then move on to more advanced topics including javascript backend development with Node.js, NoSQL database design with MongoDB, cloud computing, and re-sponsive web design. Finally, we cover advanced topics including the design and im- plementation of browser extensions and real-time web technologies like WebRTC and WebSockets. Consent of Instructor required.', 'None', 'SP24, SP25'),
#     ('CS419', 'Computing Ethics and Social Implications of Computing', 1, 'An overview of ethics for computing majors includes: history of computing, intellectual property, privacy, ethical frameworks, professional ethical responsibilities, and risks of computer-based systems.', 'CS371', 'SP24, SP25'),
#     ('CS448', 'Senior Project', 4, 'Capstone course in which C S majors work in teams and apply computer science skills to complete a large project. Restricted to: C S majors.', 'CS370, CS371', 'FA23, SP24, FA24, SP25'),
#     ('CS471', 'Programming Language Structure I', 3, 'Syntax, semantics, implementation, and application of programming languages; abstract data types; concurrency.', 'CS370, CS371', 'SP24, SP25'),
#     ('CS474', 'Operating Systems I', 3, 'Operating system principles and structures, and interactions with architectures.', 'CS273, CS371, CS372', 'FA23, FA24'),
#     ('CS475', 'Artificial Intelligence I', 3, 'Fundamental principles and techniques in artificial intelligence systems. Intelligent Agents; solving problems by searching; local search techniques; game-playing agents; constraint satisfaction problems; knowledge representation and reasoning. Further selected topics may also be covered.', 'CS272, CS278', 'SP24, SP25'),
#     ('CS477', 'Digital Game Design', 3, 'An introduction to digital game design. Topics include design, development, and playtesting of games. The course is structured to use team-based learning.', 'CS371', 'FA23, FA24'),
#     ('CS478', 'Computer Security', 3, 'Introduction to the art and science of computer security. Fundamentals of computer security including elementary cryptography, authentication and access control, security threats, attacks, detection and prevention in application software, operating systems, networks and databases.', 'CS272, CS273', 'SP24, SP25'),
#     ('CS480', 'Linux System Administration', 3, 'Basic system administration for Linux environments. Topics include user managements, file systems, security, backups, system monitoring, kernel configuration and other relevant aspects of system administration.', 'None', 'FA23, FA24'),
#     ('CS481', 'Visual Programming', 3, 'Design and implementation of programs using visual (i.e. dataflow or diagrammatic) programming techniques, with an emphasis on real-time data processing. Students will learn how to design visual programs, including how to handle cycles and state maintenance, and will learn to process audio, video, and other data using visual programs.', 'CS272, CS278', 'SP25'),
#     ('CS482', 'Database Management Systems I', 3, 'Database design and implementation; models of database management systems; privacy, security, protection, recovery.', 'CS272, CS278', 'FA23, SP24, FA24, SP25'),
#     ('CS484', 'Computer Networks I', 3, 'Fundamental concepts of computer communication networks: layered network architecture, network components, protocol stack and service. Example of application, transport, network and data link layers, protocols primarily drawn from the Internet (TCP, UDP, and IP) protocol multimedia networks; network management and security.', 'CS272, CS273', 'FA23, FA24'),
#     ('CS485', 'Human-Centered Computing', 3, 'Covers iterative, human-centered interface design, including prototyping and evaluation. Basics of graphic design and visualization.', 'CS371', 'FA23, FA24'),
#     ('CS486', 'Bioinformatics', 3, 'Introduction to bioinformatics and computational biology. Computational approaches to sequences analysis, protein structure prediction and analysis, and selected topics from current advances in bioinformatics.', 'CS272, CS278', 'FA23, SP25'),
#     ('CS487', 'Applied Machine Learning I', 3, 'An introductory course on practical machine learning. An overview of concepts for both unsupervised and supervised learning. Topics include classification, regression, clustering, and dimension reduction. Classical methods and algorithms such as linear regression, neural networks, support vector machines, and ensemble approaches. Recent techniques such as deep learning. Focused on applying of machine learning techniques in application domains.', 'CS272, MATH1511G', 'SP24, SP25'),
#     ('CS488', 'Introduction to Data Mining', 3, 'Techniques for exploring large data sets and discovering patterns in them. Data mining concepts, metrics to measure its effectiveness. Methods in classification, clustering, frequent pattern analysis. Selected topics from current advances in data mining.', 'CS272, CS278', 'FA23, FA24'),
#     ('CS489', 'Bioinformatics Programming', 3, 'Computer programming to analyze high-throughput molecular biology data including genomic sequences, bulk and single-cell transcriptome, epigenome, and other omics data. Quality control, library size normalization, confounding effect removal, clustering, statistical modeling, trajectory inference, and visualization.', 'None', 'FA23, SP25'),
#     ('CS491', 'Parallel Programming', 3, 'Programming of shared memory and distributed memory machines; tools and languages for parallel programming; techniques for parallel programming; parallel programming environments.', 'CS370', 'FA23'),
#     ('CS494', 'Introduction to Smart Grids', 3, 'This course is an introduction to the technologies and design strategies associated with the Smart Grid. The emphasis will be on the development of communications, energy delivery, coordination mechanisms, and management tools to monitor transmission and distribution networks. Topics include: Smart grid introduction and evolution; Power systems; Networking and transport control; Artificial intelligence & agent coordination; Data mining for smart grids.', 'CS272, EE230', 'SP25'),
#     ('CS496', 'Cloud and Edge Computing', 3, 'The course presents a top-down view of cloud computing, from applications and administration to programming and infrastructure. Its main focus is on the concepts of networking and parallel programming for cloud computing and large scale distributed systems which form the cloud infrastructure. The topics include: overview of cloud computing, cloud systems, parallel processing in the cloud, distributed storage systems, virtualization, security in the cloud, and multicore operating systems. Students will study state-of-the-art approaches to cloud computing followed by large cloud corporations, namely Google, Amazon, Microsoft, and Yahoo. Students will also apply what they learn through project developments using Amazon Web Services.', 'CS372', 'SP24, SP25'),
#     ('MATH1511G', 'Calculus I', 4, 'Limits and continuity, theory and computation of derivatives, applications of derivatives, extreme values, critical points, derivative tests, L\'Hopital\'s Rule. May be repeated up to 4 credits.', 'None', 'FA23, SP24, FA24, SP25'),
#     ('MATH1521G', 'Calculus II', 4, 'Riemann sums, the definite integral, antiderivatives, fundamental theorems, techniques of integration, applications of integrals, improper integrals, Taylor polynomials, sequences and series, power series and Taylor series.', 'MATH1511G', 'FA23, SP24, FA24, SP25'),
#     ('MATH2415', 'Linear Algebra', 3, 'Systems of equations, matrices, vector spaces and linear transformations. Applications to computer science.', 'MATH1521G', 'FA23, SP24, FA24, SP25'),
#     ('AST311', 'Statistical Applications', 3, 'Techniques for describing and analyzing economic and biological data; estimation, hypothesis testing, regression and correlation; basic concepts of statistical inference.', 'None', 'FA23, SP24, FA24, SP25'),
#     ('ENGL1110G', 'Composition I', 4, 'In this course, students will read, write, and think about a variety of issues and texts.They will develop reading and writing skills that will help with the writing required in their fields of study and other personal and professional contexts. Students will learn to analyze rhetorical situations in terms of audience, contexts, purpose, mediums, and technologies and apply this knowledge to their reading and writing. They will also gain an understanding of how writing and other modes of communication work together for rhetorical purposes. Students will learn to analyze the rhetorical context of any writing task and compose with purpose, audience, and genre in mind. Students will reflect on their own writing processes, learn to workshop drafts with other writers,and practice techniques for writing, revising, and editing.', 'None', 'FA23, SP24, FA24, SP25'),
#     ('ENGL2210G', 'Professional & Technical Communcation', 3, 'Professional and Technical Communication will introduce students to the different types of documents and correspondence that they will create in their professional careers. This course emphasizes the importance of audience, document design, and the use of technology in designing, developing, and delivering documents.This course will provide students with experience in professional correspondence and communicating technical information to a non-technical audience.', 'ENGL1110G', 'FA23, SP24, FA24, SP25'),
#     ('COMM1115G', 'Introduction to Communication', 3, 'This survey course introduces the principles of communication in the areas of interpersonal, intercultural, small group, organizational, public speaking, mass, and social media. May be repeated up to 3 credits.', 'None', 'FA23, SP24, FA24, SP25'),
#     ('LabScience', 'Lab Science', 4, 'This is a placeholder for a general lab science course requirement. It could be Biology, Geology, Astronomy, Physics, Etc.', 'None', 'FA23, SP24, FA24, SP25'),
#     ('VWW', 'Viewing a Wider World', 3, 'This is a placeholder for any course the university considers \'Viewing a Wider World\'', 'None', 'FA23, SP24, FA24, SP25')]
    
# cursor.executemany('INSERT INTO schedules VALUES (?,?,?,?,?)', schedules)
# cursor.executemany('INSERT INTO course_list VALUES (?,?,?,?,?,?)', course_list)


connection.commit()


connection.close()