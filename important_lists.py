PATH='' # COMPLETE HERE WITH THE PATH WHERE THE SUBTITLES WILL BE STORAGED.
DATABASE_PATH='' #COMPLETE HERE WITH THE DATABASE PATH.
DATABASE_NAME='' #COMPLETE HERE WITH THE NAME OF THE DATABASE. IT MUST INCLUDE THE FILE EXTENSION.
YOUTUBE_DATA_API_V3="" #COMPLETE HERE THE YOUTUBES DATA API KEY.
ANALYTICS_CAPTURED_ON='' #COMPLETE HERE WHEN THE DataCapture function was excecuted (ex: 2021-04-09 - YYYY/MM/DD)

#OTHER LISTS.

categories=['Activism', 'Addiction', 'Adventure', 'Advertising', 'Africa', 'Aging', 'Agriculture', 'AI', 'AIDS', 'Aircraft', 'Algorithm', 'Alternative energy', "Alzheimer's", 'Ancient world', 'Animals', 'Animation', 'Antarctica', 'Anthropocene', 'Anthropology', 'Ants', 'Apes', 'Archaeology', 'Architecture', 'Art', 'Arts', 'Asia', 'Asteroid', 'Astrobiology', 'Astronomy', 'Atheism', 'Audacious Project', 'Augmented reality', 'Autism', 'Autism spectrum disorder', 'Bacteria', 'Beauty', 'Bees', 'Behavioral economics', 'Best of the Web', 'Big bang', 'Big problems', 'Biodiversity', 'Bioethics', 'Biology', 'Biomechanics', 'Biomimicry', 'Bionics', 'Biosphere', 'Biotech', 'Birds', 'Blockchain', 'Body language', 'Books', 'Botany', 'Brain', 'Brand', 'Brazil', 'Buddhism', 'Bullying', 'Business', 'Cancer', 'Capitalism', 'Cars', 'Cello', 'Charter for compassion', 'Chemistry', 'Children', 'China', 'Choice', 'Christianity', 'Cities', 'Climate change', 'Cloud', 'Code', 'Cognitive science', 'Collaboration', 'Comedy', 'Communication', 'Community', 'Compassion', 'Complexity', 'Composing', 'Computers', 'Conducting', 'Consciousness', 'Conservation', 'Consumerism', 'Cooperation', 'Coral reefs', 'Coronavirus', 'Corruption', 'Cosmos', 'Countdown', 'Creativity', 'Crime', 'Criminal Justice', 'CRISPR', 'Crowdsourcing', 'Cryptocurrency', 'Culture', 'Curiosity', 'Cyborg', 'Dance', 'Dark matter', 'Data', 'Death', 'Debate', 'Decision-making', 'Deextinction', 'Demo', 'Democracy', 'Depression', 'Design', 'Development', 'Dinosaurs', 'Disability', 'Disaster relief', 'Discovery', 'Disease', 'Diversity', 'DNA', 'Driverless cars', 'Drones', 'Ebola', 'Ecology', 'Economics', 'Education', 'Egypt', 'Electricity', 'Emotions', 'Empathy', 'Encryption', 'Energy', 'Engineering', 'Entertainment', 'Entrepreneur', 'Environment', 'Epidemiology', 'Europe', 'Evil', 'Evolution', 'Evolutionary psychology', 'Exercise', 'Exoskeleton', 'Exploration', 'Extraterrestrial life', 'Extreme sports', 'Failure', 'Faith', 'Family', 'Farming', 'Fashion', 'Fear', 'Feminism', 'Film', 'Finance', 'Fish', 'Flight', 'Food', 'Foreign Policy', 'Forensics', 'Friendship', 'Fungi', 'Funny', 'Future', 'Gaming', 'Garden', 'Gender', 'Gender equality', 'Gender spectrum', 'Genetics', 'Geology', 'Glacier', 'Global commons', 'Global development', 'Global issues', 'Goal-setting', 'God', 'Google', 'Government', 'Grammar', 'Graphic design', 'Green', 'Guitar', 'Guns', 'Hack', 'Happiness', 'Health', 'Health care', 'Healthcare', 'Hearing', 'Heart health', 'Hinduism', 'History', 'HIV', 'Homelessness', 'Human body', 'Human origins', 'Human rights', 'Humanities', 'Humanity', 'Humor', 'Identity', 'Illness', 'Illusion', 'Immigration', 'Inclusion', 'India', 'Indigenous peoples', 'Industrial design', 'Inequality', 'Infrastructure', 'Innovation', 'Insects', 'Intelligence', 'Interface design', 'Internet', 'Interview', 'Introvert', 'Invention', 'Investment', 'Iran', 'Iraq', 'Islam', 'Jazz', 'Journalism', 'Judaism', 'Justice system', 'Language', 'Latin America', 'Law', 'Leadership', 'LGBT', 'Library', 'Life', 'Literature', 'Live music', 'Love', 'MacArthur grant', 'Machine learning', 'Magic', 'Manufacturing', 'Map', 'Marine biology', 'Marketing', 'Markets', 'Mars', 'Materials', 'Math', 'Media', 'Medical imaging', 'Medical research', 'Medicine', 'Meditation', 'Meme', 'Memory', 'Men', 'Mental health', 'Microbes', 'Microbiology', 'Microfinance', 'Microsoft', 'Middle East', 'Military', 'Mind', 'Mindfulness', 'Mining', 'Mission blue', 'Mobility', 'Molecular biology', 'Money', 'Monkeys', 'Moon', 'Morality', 'Motivation', 'Movies', 'Museums', 'Music', 'Nanoscale', 'Narcotics', 'NASA', 'Natural disaster', 'Natural resources', 'Nature', 'Neurology', 'Neuroscience', 'New York', 'News', 'Nobel prize', 'Nonviolence', 'Novel', 'Nuclear energy', 'Nuclear weapons', 'Obesity', 'Oceans', 'Oil', 'Online video', 'Open-source', 'Opioids', 'Origami', 'Pain', 'Painting', 'Paleontology', 'Pandemic', 'Parenting', 'Peace', 'Performance', 'Performance art', 'Person', 'Personal growth', 'Personality', 'Pharmaceuticals', 'Philanthropy', 'Philosophy', 'Photography', 'Physics', 'Physiology', 'Piano', 'Planets', 'Plants', 'Plastic', 'Play', 'Poetry', 'Policy', 'Politics', 'Pollution', 'Population', 'Potential', 'Poverty', 'Prediction', 'Pregnancy', 'Presentation', 'Primates', 'Prison', 'Privacy', 'Product design', 'Productivity', 'Programming', 'Prosthetics', 'Protests', 'Psychology', 'PTSD', 'Public health', 'Public spaces', 'Quantum physics', 'Race', 'RAP', 'Refugees', 'Relationships', 'Religion', 'Resources', 'Rivers', 'Robots', 'Rocket science', 'Sanitation', 'Science', 'Science and art', 'Science Fiction', 'Security', 'Self', 'Senses', 'Sex', 'Sexual violence', 'Shopping', 'Sight', 'Simplicity', 'Singer', 'Skateboarding', 'Slavery', 'Sleep', 'Smell', 'Social change', 'Social media', 'Social science', 'Social Sciences', 'Society', 'Sociology', 'Software', 'Solar energy', 'Solar system', 'Sound', 'South America', 'Space', 'Speech', 'Spoken word', 'Sports', 'Start-up', 'State-building', 'Statistics', 'Stigma', 'Storytelling', 'Street art', 'String theory', 'Student', 'Submarine', 'Success', 'Suicide', 'Sun', 'Surgery', 'Surveillance', 'Sustainability', 'Synthetic biology', 'Syria', 'Teaching', 'Technology', 'TED Books', 'TED Connects', 'TED en Español', 'TED Fellows', 'TED Prize', 'TED Residency', 'TED-Ed', 'TEDMED', 'TEDNYC', 'TEDx', 'TEDYouth', 'Telecom', 'Telescopes', 'Television', 'Terrorism', 'Theater', 'Time', 'Toy', 'Trafficking', 'Transgender', 'Transportation', 'Travel', 'Trees', 'Trust', 'Typography', 'United States', 'Universe', 'Urban', 'Urban planning', 'Vaccines', 'Violence', 'Violin', 'Virtual reality', 'Virus', 'Visualizations', 'Vocals', 'Vulnerability', 'War', 'Water', 'Weather', 'Web', 'Wikipedia', 'Wind energy', 'Women', 'Women in business', 'Work', 'Work-life balance', 'World cultures', 'Writing', 'Wunderkind', 'Youth', '3d printing']

countries_list=['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', "Côted Ivoire", 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Democratic Republic of the Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Holy See', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'SriLanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']

stopwords="'ive','didnt','actually','lot','tell','didnt','youve','oh','weve','a','am','about', 'above', 'across', 'after', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'among', 'an', 'and', 'another', 'any', 'anybody', 'anyone', 'anything', 'anywhere', 'are', 'area', 'areas', 'around', 'as', 'ask', 'asked', 'asking', 'asks', 'at', 'away', 'b', 'back', 'backed', 'backing', 'backs', 'be', 'became', 'because', 'become', 'becomes', 'been', 'before', 'began', 'behind', 'being', 'beings', 'best', 'better', 'between', 'big', 'both', 'but', 'by', 'c', 'came', 'can', 'cannot', 'case', 'cases', 'certain', 'certainly', 'clear', 'clearly', 'come', 'could', 'd', 'did', 'differ', 'different', 'differently', 'do', 'does', 'done', 'down', 'down', 'downed', 'downing', 'downs', 'during', 'e', 'each', 'early', 'either', 'end', 'ended', 'ending', 'ends', 'enough', 'even', 'evenly', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'f', 'face', 'faces', 'fact', 'facts', 'far', 'felt', 'few', 'find', 'finds', 'first', 'for', 'four', 'from', 'full', 'fully', 'further', 'furthered', 'furthering', 'furthers', 'g', 'gave', 'general', 'generally', 'get', 'gets', 'give', 'given', 'gives', 'go', 'going', 'good', 'goods', 'got', 'great', 'greater', 'greatest', 'group', 'grouped', 'grouping', 'groups', 'h', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'herself', 'high', 'high', 'high', 'higher', 'highest', 'him', 'himself', 'his', 'how', 'however', 'i', 'if', 'important', 'in', 'interest', 'interested', 'interesting', 'interests', 'into', 'is', 'it', 'its', 'itself', 'j', 'just', 'k', 'keep', 'keeps', 'kind', 'knew', 'know', 'known', 'knows', 'l', 'large', 'largely', 'last', 'later', 'latest', 'least', 'less', 'let', 'lets', 'like', 'likely', 'long', 'longer', 'longest', 'm', 'made', 'make', 'making', 'man', 'many', 'may', 'me', 'member', 'members', 'men', 'might', 'more', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', 'my', 'myself', 'n', 'necessary', 'need', 'needed', 'needing', 'needs', 'never', 'new', 'new', 'newer', 'newest', 'next', 'no', 'nobody', 'non', 'noone', 'not', 'nothing', 'now', 'nowhere', 'number', 'numbers', 'o', 'of', 'off', 'often', 'old', 'older', 'oldest', 'on', 'once', 'one', 'only', 'open', 'opened', 'opening', 'opens', 'or', 'order', 'ordered', 'ordering', 'orders', 'other', 'others', 'our', 'out', 'over', 'p', 'part', 'parted', 'parting', 'parts', 'per', 'perhaps', 'place', 'places', 'point', 'pointed', 'pointing', 'points', 'possible', 'present', 'presented', 'presenting', 'presents', 'problem', 'problems', 'put', 'puts', 'q', 'quite', 'r', 'rather', 'really', 'right', 'right', 'room', 'rooms', 's', 'said', 'same', 'saw', 'say', 'says', 'second', 'seconds', 'see', 'seem', 'seemed', 'seeming', 'seems', 'sees', 'several', 'shall', 'she', 'should', 'show', 'showed', 'showing', 'shows', 'side', 'sides', 'since', 'small', 'smaller', 'smallest', 'so', 'some', 'somebody', 'someone', 'something', 'somewhere', 'state', 'states', 'still', 'still', 'such', 'sure', 't', 'take', 'taken', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'therefore', 'these', 'they', 'thing', 'things', 'think', 'thinks', 'this', 'those', 'though', 'thought', 'thoughts', 'three', 'through', 'thus', 'to', 'today', 'together', 'too', 'took', 'toward', 'turn', 'turned', 'turning', 'turns', 'two', 'u', 'under', 'until', 'up', 'upon', 'us', 'use', 'used', 'uses', 'v', 'very', 'w', 'want', 'wanted', 'wanting', 'wants', 'was', 'way', 'ways', 'we', 'well', 'wells', 'went', 'were', 'what', 'when', 'where', 'whether', 'which', 'while', 'who', 'whole', 'whose', 'why', 'will', 'with', 'within', 'without', 'work', 'worked', 'working', 'works', 'would', 'x', 'y', 'year', 'years', 'yet', 'you', 'young', 'younger', 'youngest', 'your', 'yours', 'z',''"
