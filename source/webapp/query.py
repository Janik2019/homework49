from webapp.models import Project, Task,Type, Status
from datetime import datetime, timedelta



project = Task.objects.filter(project__title='Блог')
project.values('task__type__type')


project = Task.objects.filter(decscription__icon='Блог')
