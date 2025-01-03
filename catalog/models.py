from django.db import models
from django.urls import reverse
import uuid

class Language(models.Model):
    language = models.CharField(max_length=50, unique=True,  help_text='Введите язык на котором напечатана книга(Русскийб анлийскийб японский и тд)')

    def __str__(self):
        return self.language
    
    def get_absolute_url(self):
        return reverse('language-detail', args=[str(self.id)] )

class Genre(models.Model):
    name = models.CharField(max_length=20, help_text='Enter a book genre(e.g. French poetry, Science fantastic etc.)')

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(verbose_name='Описание', max_length=1000, help_text='Введи описание книги')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text='Введите жанр книги')
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Жанр'
    # short_description указывает как будет называться данная функция в админ панели если мы ее укажем показывать на панели в admin.py
    class Meta:
        ordering = ['title']    

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, help_text='ID для каждой книги индивидуален в библиотеке' )
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    

    LOAN_STATUS = (
        ('m', 'Maintenance(Техническое обслуживание)'),
        ('o', 'On loan(На руках)'),
        ('a', 'Available(Доступна для бронирования)'),
        ('r', 'Reserved(Зарезервирована)')
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='m', blank=True, help_text='Доступность экземпляра на данный момент')

    class Meta:
        ordering = ['-due_back']

    def __str__(self):
        return '{0} - {1}'.format(self.id,self.book.title)
    
    def get_absolute_url(self):
        return reverse('BookInstance-detail', args = [str(self.id)])
    
    # def display_book(self):
    #     return self.book
    # display_book.short_description = 'Название'
    
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
    
    class Meta:
        ordering = ['last_name']