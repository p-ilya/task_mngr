from django.db import models
# from django.forms import TimeInput
# Create your models here.


class Task(models.Model):
    '''
    Абстрактный класс задачи.
    '''
    name = models.CharField(
        max_length=300,
        help_text='Что нужно сделать?')

    priority = models.ForeignKey(
        'Priority',
        null=True,
        on_delete=models.SET_NULL)

    tags = models.ManyToManyField('Tag')

    done = models.BooleanField(
        default=False)

    class Meta:
        abstract = True
        ordering = ['priority', 'name']

    def __str__(self):
        return self.name


class DayTask(Task):
    '''
    Дело, имеющее конкретную дату
    и, возможно, время выполнения.
    '''
    task_date = models.DateField()
    task_time = models.TimeField()

    class Meta:
        verbose_name = 'дело на дату'
        verbose_name_plural = 'дела на дату'


class IntervalTask(Task):
    '''
    Дело, которое нужно выполнить до какого-либо срока.
    Начальный срок по умолчанию - текущее число.
    '''
    start_date = models.DateField(auto_now=True)
    due_date = models.DateField()

    class Meta:
        verbose_name = 'дело до даты'
        verbose_name_plural = 'дела до даты'


class SimpleTask(Task):
    '''
    Просто дело, без срока.
    '''
    why = models.TextField(
        help_text='''Здесь можно написать заметку-мотиватор.
        Почему это нужно сделать? Что это принесет?''')

    class Meta:
        verbose_name = 'простое дело'
        verbose_name_plural = 'простые дела'


class Priority(models.Model):
    ''' Класс, описывающий категории приоритета. '''
    level = models.CharField(
        max_length=30,
        help_text='Название категории приоритета')

    importance = models.IntegerField(
        help_text='Int. Меньше - важнее дело.',
        null=True)

    class Meta:
        ordering = ['importance']
        verbose_name = 'приоритет'
        verbose_name_plural = 'приоритеты'

    def __str__(self):
        return self.level


class Tag(models.Model):
    ''' Простые текстовые тэги. '''
    name = models.CharField(
        max_length=30,
        help_text='Имя тэга')

    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'

    def __str__(self):
        return self.name