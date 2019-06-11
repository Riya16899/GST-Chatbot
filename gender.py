import random
from nltk import NaiveBayesClassifier
from nltk.classify import accuracy as nltk_accuracy
from nltk.corpus import names

# Extract last N letters from the input word
# and that will act as our "feature"
def extract_features(word, N=2):
  last_n_letters = word[-N:]
  return {'feature': last_n_letters.lower()}

if __name__=='__main__':
# Create training data using labeled names available in NLTK
  male_list = [(name, 'male') for name in names.words('male.txt')]
  female_list = [(name, 'female') for name in names.words('female.txt')]
  data = (male_list + female_list)
  # Seed the random number generator
  random.seed(5)
# Shuffle the data
  random.shuffle(data)
  input_names = ['Riya', 'dharmit', 'David', 'Cheryl']

# Define the number of samples used for train and test
  num_train = int(0.8 * len(data))

for i in range(1, 6):
  print('\nNumber of end letters:', i)
  features = [(extract_features(n, i), gender) for (n, gender) in data]
  train_data, test_data = features[:num_train], features[num_train:]
  classifier = NaiveBayesClassifier.train(train_data)
  accuracy = round(100 * nltk_accuracy(classifier, test_data), 2)
  #print('Accuracy = ' + str(accuracy) + '%')

for name in input_names:
  print(name, '==>', classifier.classify(extract_features(name, i)))
























while True:


	if first_ask in army:
		x = raw_input(">>>")  
		userinput = x.lower()

		Stop_Word().stop_word(z,x)
		print(z)
		Spell(z,z1)
		print(z1)
		for j in z1:
			if j in army_readd:
				print("army")
			elif j not in army_readd:
				print("another")

	elif first_ask in navy:
		x = raw_input(">>>")  
		userinput = x.lower()

		Stop_Word().stop_word(z,x)
		print(z)
		Spell(z,z1)
		for j in z1:
			if j in navy_readd:
				print("navy")
			elif j not in navy_readd:
				print("another")

	elif first_ask in air_force:
		x = raw_input(">>>")  
		userinput = x.lower()

		Stop_Word().stop_word(z,x)
		print(z)
		Spell(z,z1)
		for j in z1:
			if j in air_force_readd:
				print("air_force")
			elif j not in air_force_readd:
				print("another")


	break
