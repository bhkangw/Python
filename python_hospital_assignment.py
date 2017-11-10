# Assignment: Hospital
# You're going to build a hospital with patients in it! Create a hospital class.

# Before looking at the requirements below, think about the potential characteristics of each patient and hospital. 
# How would you design each?

# Patient:
# Attributes:
	# Id: an id number
	# Name
	# Allergies
	# Bed number: should be none by default

# Hospital:
# Attributes:
	# Patients: an empty array
	# Name: hospital name
	# Capacity: an integer indicating the maximum number of patients the hospital can hold.

# Methods:
	# Admit: add a patient to the list of patients. Assign the patient a bed number. 
	# 	If the length of the list is >= the capacity do not admit the patient. 
	# 	Return a message either confirming that admission is complete or saying the hospital is full.
	# Discharge: look up and remove a patient from the list of patients. 
	#	Change bed number for that patient back to none.

# Ask yourself what input each method requires and what output you will need.

class Patient(object):
	patient_number = 1
	def __init__(self, name, *allergies):
		self.id = Patient.patient_number
		self.name = name
		self.allergies = allergies
		self.bed_number = None
		Patient.patient_number +=1

	def display_info(self):
		print "ID: " + str(self.id)
		print "Name: " + str(self.name)
		print "Allergies: " + str(self.allergies).join(self.allergies)
		print "Bed #: " + str(self.bed_number)

class Hospital(object):
	def __init__(self):
		self.patients = []
		self.name = "Seattle Grace"
		self.capacity = 5
		self.beds = self.bed_info()

	def bed_info(self):
		beds = []
		for i in range(0, 5):
			beds.append({
				"bed_id": i,
				"Available" : True
			})
		return beds

	# def admit(self, new_patient):
	# 	Hospital.bed_number = 4
	# 	self.patients.append(new_patient)
	# 	if len(patients) <= self.capacity:
	# 		self.bed_number = Hospital.bed_number
	# 		Hospital.bed_number +=1
	# 		print "Admission is complete!"
	# 	else:
	# 		print "Sorry hospital is full"

	def admit(self, patient):
		if len(self.patients) <= self.capacity:
			self.patients.append(patient)
			for i in range(0, len(self.beds)):
				if self.beds[i]["Available"]:
					patient.bed_num = self.beds[i]["bed_id"]
					self.beds[i]["Available"] = False
					break
			print "Patient #{} admitted to bed #{}".format(patient.id, patient.bed_num)
			# print "Patient " + patient.id + "admitted to bed " + patient.bed_number # same as above
		else:
			print "Sorry hospital is full"

	def discharge(self, patient):
		for patient in self.patients:
			if patient.id == patient_id:
				for bed in self.beds:
					if bed["bed_id"] == patient.bed_num:
						bed["Available"] = True
						break
				self.patients.remove(patient)
				return "Patient #{} sucessfully discharged. Bed #{} now available".format(patient.id, patient.bed_num)
				# return "Patient " + patient.id + " sucessfully discharged. Bed " + patient.bed_num + " now available"
		return "Patient not found"

patient1 = Patient("Brian","none")
# patient1.display_info()

patient2 = Patient("Joe","none")
# patient2.display_info()

patient3 = Patient("Me","none")
# patient3.display_info()

patient4 = Patient("You","none")
# patient4.display_info()

patient5 = Patient("No","none")
# patient5.display_info()

patient6 = Patient("No","none")
# patient6.display_info()

hosp1 = Hospital()
print hosp1.admit(patient1)

hosp2 = Hospital()
print hosp2.admit(patient2)

hosp3 = Hospital()
print hosp3.admit(patient3)

hosp4 = Hospital()
print hosp4.admit(patient4)

hosp5 = Hospital()
print hosp5.admit(patient5)

hosp6 = Hospital()
print hosp6.admit(patient6)














