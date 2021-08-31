
* [annotation_system](annotation_system.md)




* syntax : 5mins
	* start 14:49
	* summary :
		* task filter command modification miscellaneous
		* [filter] [modification] [miscellaneous] are all parameter of command
		* some command only accept several sort of them
		* four of them all have default values
		* Overide can put anywhere to overide config temporarily
	* end 14:59
* bastpractice : 5 mins
	* start 14:59
	* summary:
		* task config urgency.user.tag.problem.coefficient 4.5
		* task config urgency.user.project.Home.coefficient 2.9
	* end 15:20

* example commands : 10 mins
	* start 15:21
	* summary:
		* sort:
			* mulitple line discription ""
			* task entry.after:now-1hour list
			* task end.after:2015-01-01 list
			* task end.yesterday
			* task project:vim and \( priority:H or priority:M \)
			* task rc.search.case.sensitive:no  /pattern/ list
		* reports: a collection of configurations:
			* task rc.report.next.sort=due-,urgency- next
			* the former one will override temporarily
		* projects:
			* task project:old_name modify project:new_name
			* project Hierarchy:
				* task add project:home.kitchen Clean the floor
				* task project:home.kitchen count
				* task project:home count
		* tags:
			* task tag.none: list
			* virtual tags:
				* +DUETODAY +OVERDUE +WEEK +TODAY
		* recurring tasks:
			* task add Do the thing due:2015-06-08T09:00 recur:weekly
			* task add Pay rent due:28th recur:monthly until:now+1yr
			* the former one only recur for one year
		* priority: can be configed:
			* task config -- uda.priority.values H,M,,L
			* task config -- uda.priority.values pr1,pr2,pr3,pr4,pr5,pr6
		* color:configrable:
			* one day I shall look carefully into how to use it
			* to group my task tags and projects
		* DOM:easy to access all attribute of all tasks in database:
			* task _get 12(it's a task id).entry 12.modification
			* task add task13 due:12.due
			* the former one will use task 12's due date
	* end 15:43
* workflow : 5 mins
	* start 15:44
	* summary:
	* end 16:02
* all commands : 5 mins
	* start 16:02
	* summary:
	* end 16:12

* date : 10 mins:
	* summary:
		* due : time must be donw
		* schedule : time can start doing
		* wait : time task start to show on list
		* until date : time when the task self-destruct
	* end 16:17
	
* reports : 15 mins:
	* start 16:17
	* summary:
		* modify report:
			* task show report.next.lables
			* task show report.next.columns
			* lables are lable of columns
			* task config report.next.lables 'ID,Project,Description'
		* customize report:
			* give value to:
				* discription
				* lables
				* columns:
					* task _columns
				* sort
				* filter
	* end 16:48

* filters : 10 mins:
	* start 16:48
	* summary:
	* end 16:52

* priority : 5 mins:
	* start 16:52
	* summary:
		* color.uda.priority.H=color255
		* uda.priority.values=H,M,L,
		* urgency.uda.priority.H.coefficient=6.0
	* end 16:55

* tags and virtual tags : 5 mins:
	* start 16:56
	* summary:
	* end 16:57

* date and time : 10 mins:

* named dates : 5 mins:

* duration : 5 mins:

* configuartion : 10 mins:
	* start 17:01
	* summary:
		* support include and sub include
		* env:
			* TASKRC
			* TASKDATA
	* end 17:04
* terminology : 15 mins:
	* start 17:04
	* summary:
		* alias
	* end 17:10

* urgency : 10 mins: (skim)

* context : 10 mins:
	* start 17:26
	* summary:
		* A context is associated with a location
		* task context define work +work or +freelance
		* task context define home -work -freelance -school -homework -lab
		* To set or switch the current context, simply:
		* task context home
		* task context show
		* task context none
* recurrence : 5 mins:

* uda : 15 mins: (watch when use)

* external : 25 mins:
	* start 23:07
	* summary:
		* look into taskopen for knowledge base build
* DOM : 15 mins: (skim through)

