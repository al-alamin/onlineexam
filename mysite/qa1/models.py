from __future__ import unicode_literals
from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

# from readingmaterial.models import ReadingTopic
# from readingmaterial.models import SubTopic1, ReadingTopic, ReadingContent
from readingmaterial.models import *
from subscription.models import *
from django.utils.html import format_html
from django.utils.html import mark_safe
from django.contrib.humanize.templatetags.humanize import naturaltime 



# class ReadingContentInline(admin.TabularInline):
#     model = ReadingContent
#     extra = 0



class Question_Topic(models.Model):   
    question_topic_text = models.CharField(max_length=200, blank=True, null=True)       
    is_reading_content = models.BooleanField("Is Topic Wise",default=False)
    def __unicode__(self):
        return self.question_topic_text

    class Meta:
        verbose_name="Question Topic List"





class Question_Set(models.Model):  
    question_set_text = models.CharField(max_length=200, verbose_name="Question Set")  
    question_topic = models.ForeignKey(Question_Topic,blank=True, null=True) 
    
    # reading_contents = models.ManyToManyField(ReadingContent)
    subtopic1 = models.ForeignKey(SubTopic1, blank=True, null=True, verbose_name="Sub Topic Name")
    reading_topic = models.ForeignKey(ReadingTopic,  blank=True, null=True)

    # mcq_question = models.ManyToManyField(Mcq_Question, blank=True, null=True)  
    # reading_content = models.ForeignKey(ReadingContent, blank=True, null=True)

    pub_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    edit_date = models.DateTimeField('Editing Date: ', blank=True, null=True)

    start_date = models.DateTimeField('Exam Start Date: ', blank=True, null=True)
    end_date = models.DateTimeField('Exam End Date: ', blank=True, null=True)



    uploader = models.ForeignKey(User, blank=True, null=True)

    individual_mcq_marks = models.IntegerField("Individual Mcq Question Marks: ", default=1) 
    negative_marking_percentage = models.IntegerField("Percent Of Marks To Be Deducted For Wrong Answer: ", default=0) 

    individual_mcq_time = models.IntegerField("Individual Mcq Question Time In Second: ", default=60) 


    is_free = models.BooleanField("Is Free",default=True)
    subscription_plan = models.ManyToManyField(Subscription_Plan, blank=True, null=True )
    # special_plan = models.ManyToManyField(Special_Plan, blank=True, null=True)
    reading_content = models.ManyToManyField(ReadingContent, blank=True, null=True)
    # is_free2 = models.BooleanField("Is Free",default=True)

    def update_date(self):
        if (not self.pub_date):
            self.pub_date = timezone.now()

        self.edit_date = timezone.now()
        self.save() 

    def can_publish(self):

        if (self.start_date):                
            now = timezone.now()
            if (now < self.end_date):
                return False
        return True


    # def get_marks(self):
    #     print ("****** get marks method")
    #     result = Question_Set_Result.objects.filter(question_set=self).first()
    #     print (self.user)
    #     # print (request.user)

    #     print ("****** users printed")



    #     # return result.marks



    #     return 3
        


        
    def __unicode__(self):
        return (self.question_set_text)

    class Meta:
        verbose_name="Question Set"





class Mcq_Question(models.Model):
    # question_set = models.ManyToManyField(Question_Set, blank=True, null=True) 
    # subject_set = models.ManyToManyField(Subject, blank=True, null=True)
    # tag_set = models.ManyToManyField(Tag, blank=True, null=True)

    question_text = models.CharField(max_length=400)   
    mcq_image = models.ImageField(upload_to='images/mcq/', blank=True, null=True)
    choice_a =  models.CharField(max_length=200) 
    choice_b =  models.CharField(max_length=200) 
    choice_c =  models.CharField(max_length=200) 
    choice_d =  models.CharField(max_length=200) 


    choice_e =  models.CharField(max_length=200, blank=True, null=True) 
    choice_f =  models.CharField(max_length=200, blank=True, null=True) 
    

    mcq_answer = models.CharField(max_length=200)  
    # mcq_answer2 = models.CharField(max_length=200, blank=True, null=True)

    tag1 = models.CharField(max_length = 100, blank=True, null=True)
    tag2 = models.CharField(max_length=100, blank=True, null=True)
    tag3 = models.CharField(max_length=100, blank=True, null=True)
    tag4 = models.CharField(max_length=100, blank=True, null=True)
    tag5 = models.CharField(max_length=100, blank=True, null=True)

    # tag_topic = models.CharField(max_length=100, blank=True, null=True)
    # tag_sub_topic = models.CharField(max_length=100, blank=True, null=True)
    # tag_content = models.CharField(max_length=100, blank=True, null=True)

    # tag_inconsistent = models.CharField(max_length=200, blank=True, null=True)






    explanation_text = models.TextField( blank=True, null=True)
    explanation_image = models.ImageField(upload_to='images/mcq/', blank=True, null=True)

    pub_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    edit_date = models.DateTimeField('Editing Date: ', blank=True, null=True)

    uploader = models.ForeignKey(User, blank=True, null=True)


    question_set = models.ForeignKey(Question_Set)
    subtopic1 = models.ForeignKey(SubTopic1, blank=True, null=True,
        verbose_name='Sub-Topic')
    reading_topic = models.ForeignKey(ReadingTopic, blank=True, null=True,
        verbose_name='Topic ')

    reading_content = models.ForeignKey(ReadingContent, blank=True, null=True,
        verbose_name='Reading Content  ')


    def update_date(self):
        if (not self.pub_date):
            self.pub_date = timezone.now()

        self.edit_date = timezone.now()
        self.save()  





    def __unicode__(self):
        return  self.question_text
    
    def get_question_text(self):
        return mark_safe('%s' % self.question_text)

    def get_pub_date(self):
        return naturaltime(self.pub_date)



    class Meta:
        verbose_name=" Individual MCQ Questions "














class MarkedText(models.Model):
    marked_text = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, blank=True)


    def __unicode__(self):
        return self.marked_text



class Marked_Mcq(models.Model):
    user = models.ForeignKey(User)
    mcq_question = models.ForeignKey(Mcq_Question)
    # content = models.ForeignKey(ReadingContent, null=True, blank=True)

    # def __unicode__(self):
    #     return ("user: %s mcq_question: %s " %(self.user, self.mcq_question))

    class Meta:
        unique_together = ('user', 'mcq_question',)




class Question_Set_Result(models.Model):  
    user = models.ForeignKey(User)    
    question_set = models.ForeignKey(Question_Set)    


    start_date = models.DateTimeField('Publishing Date: ')
    finish_date = models.DateTimeField('Editing Date: ')
    can_publish = models.BooleanField("Can Pulbish Result Now: ",default=True)

    marks =  models.FloatField(blank=True, null=True)
    position  =  models.IntegerField("Position", default=0) 


    def update_date(self):
        # if (not self.pub_date):
        #     self.pub_date = timezone.now()

        # self.edit_date = timezone.now()

        self.save() 

    def update_can_publish(self):
        if (self.question_set.start_date):
            now = timezone.now()
            # print (self.question_set.end_date)

            if (now >= self.question_set.end_date):
                self.can_publish = True                 
            else:
                self.can_publish = False
            self.save()



        # self.edit_date = timezone.now()

        # self.save() 


        
    def __unicode__(self):
        return self.question_set.question_set_text

    class Meta:
        verbose_name="Result"
        unique_together = ('user', 'question_set',)