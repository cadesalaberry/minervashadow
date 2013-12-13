import json

class jsonObject(object):
	def json(self):
		return json.dumps(self.__dict__, default=lambda o: o.__dict__)

class minervaSite(jsonObject):
	def __init__(self, _baseURL='https://horizon.mcgill.ca/pban1/'):
		self.base = _baseURL
		self.login = _baseURL + 'twbkwbis.P_ValLogin'
		self.logout = _baseURL + 'twbkwbis.P_Logout'
		self.search = _baseURL + 'bwckgens.p_proc_term_date'
		self.transcript = _baseURL + 'bzsktran.P_Display_Form?user_type=S&tran_type=V'
		self.quick_search = _baseURL + 'bwskfreg.P_AltPin'
		self.result = _baseURL + 'twbkwbis.P_Logout'


class minervaCred(jsonObject):
	def __init__(self, _mail, _password):
		self.usermail = _mail
		self.password = _password
		self.loggedin = False

	def __repr__(self):
		return '<Credentials of: %s>' % self.usermail


class minervaCourse(jsonObject):
	def __init__(self, _subject):
		self.grade = None
		self.title = None
		self.number = None
		self.earned = None
		self.subject = _subject
		self.credits = None
		self.remarks = None
		self.average = None

	def __repr__(self):
		return "<Course: {0}>".format(self.subject)

	def __str__(self):
		course = self
		string = '\n    ' + repr(course)
		return string

	def addCourse(self, course):
		self.courses.append(course)


class minervaSemester(jsonObject):
	def __init__(self, _semester, _year):
		self.name = ' '.join((_year, _semester))
		self.year = _year
		self.courses = []
		self.semester = _semester
		self.standing = None
		self.advanced = []
		self.description = None

	def __repr__(self):
		return "<Semester: {0} ({1} courses)>".format(self.name, len(self.courses))

	def __str__(self):
		semester = self
		string = '\n  ' + repr(semester)

		for course in semester.courses:
			string += str(course)

		return string

	def addCourse(self, course):
		self.courses.append(course)


class minervaCurriculum(jsonObject):
	def __init__(self, _education='', _diploma=''):
		self.education = _education
		self.semesters = []
		self.diploma = _diploma
		
	def __repr__(self):
		return "<Curriculum: {0} ({1} semesters)>".format(self.diploma, len(self.semesters))

	def __str__(self):
		curriculum = self
		string = repr(curriculum)

		for semester in curriculum.semesters:
			string += str(semester)

		return string

	def addSemester(self, semester):
		self.semesters.append(semester)

	def lastSemester(self):
		if not self.semesters:
			sem = minervaSemester('Empty','Semester')
			self.addSemester(sem)
		return self.semesters[-1]

def current_semester():

	return '201401'
