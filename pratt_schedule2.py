schedule = {
	"monday" :   ['Human-Information Behavior','Information Professions','Research Mthds/Law Lit','Strategic Leadership','Conservation and Preservation','Info Services & Resources'],
	"tuesday":   ['Information Arch/Inter Design','Information Professions','Acad Libraries and Scholarly','Info Services & Resources'],
	"wednesday": ['Info Services & Resources','Usability Theory & Practice','Mgmt of Archives/Sp Collection','Government Info Sources','Library Media Centers','Mgmt of Archives/Sp Collection'],
	"thursday": ['Information Science Research','Information Professions','Information Professions'],
}
for day_week in schedule:
	for classes in schedule[day_week]:
		print ("\n",day_week,"\t",classes,"\t")
		
	
	



#loop through each day in schedule and then loop through all the class names and print them out