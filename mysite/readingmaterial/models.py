from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from qa1.models import Mcq_Question
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.utils import timezone

class ReadingTopic(models.Model):   
    reading_topic_text = models.CharField(max_length=200)       

    def __unicode__(self):
        return self.reading_topic_text


class SubTopic1 (models.Model):
    subtopic1_text = models.CharField(max_length=200)
    topic = models.ForeignKey(ReadingTopic)

    def __unicode__(self):
        return self.subtopic1_text

    class Meta:
        verbose_name = "Sub Topic Of Contents"




# class SubTopic2(models.Model):
# 	subtopic2_text = models.CharField(max_length=200)
# 	subtopic1 = models.ForeignKey(SubTopic1)

# 	def __unicode__(self):
# 		return self.subtopic2_text


class ReadingContent(models.Model):
    content_title = models.CharField(max_length=200)
    content_body = models.TextField()
    
    image1 = models.ImageField(upload_to='images/content/', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/content/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/content/', blank=True, null=True)
    image4 = models.ImageField(upload_to='images/content/', blank=True, null=True)
    image5 = models.ImageField(upload_to='images/content/', blank=True, null=True)

    mcq_question = models.ManyToManyField(Mcq_Question, blank=True, null=True)
    # mcq_question = models.ManyToManyField(Mcq_Question, blank=True, null=True)
    subtopic1 = models.ForeignKey(SubTopic1, blank=True, null=True)

	# subtopic2 = models.ForeignKey(SubTopic2, blank=True, null=True)
    reading_topic = models.ForeignKey(ReadingTopic, blank=True, null=True)

    pub_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    edit_date = models.DateTimeField('Editing Date: ', blank=True, null=True)

    uploader = models.ForeignKey(User, blank=True, null=True)



    # def save(self, *args, **kwargs):    
    #     super(ReadingContent, self).save(*args, **kwargs) # Call the "real" save() method.

    #     mcq = Mcq_Question.objects.filter(readingcontent__id = self.id)
    #     print ("these mcqs tag_content will be updated: \n")
    #     print (mcq)

        # print ("\n\n\n ****************id: content: \n" )
        # print (self.id)

    # @receiver(post_save, sender=SignaledModel)
    # def model_post_save(sender, **kwargs):
    #     print('*****************************Saved an instance with type: {}'.format(sender))

    def update_date(self):
        if (not self.pub_date):
            self.pub_date = timezone.now()

        self.edit_date = timezone.now()

        self.save() 


    def __unicode__(self):
        return self.content_title

class ContentNotes(models.Model):
    content_notes = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True)
    content = models.ForeignKey(ReadingContent, null=True, blank=True)

    def __unicode__(self):
        return self.content_notes

class ContentMarkedText(models.Model):
    marked_text = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True)
    content = models.ForeignKey(ReadingContent, null=True, blank=True)

    def __unicode__(self):
        return self.marked_text

class ContentMarkedMcq(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    mcq_question = models.ForeignKey(Mcq_Question, null=True, blank=True)
    content = models.ForeignKey(ReadingContent, null=True, blank=True)

    def __unicode__(self):
        return ("user: %s mcq_question: %s " %(self.user, self.mcq_question))



class ContentComment(models.Model):
    comment_text = models.TextField()
    user = models.ForeignKey(User)
    content = models.ForeignKey(ReadingContent)

    pub_date = models.DateTimeField('Publishing Date: ', blank=True, null=True)
    edit_date = models.DateTimeField('Editing Date: ', blank=True, null=True)


    def update_date(self):
        if (not self.pub_date):
            self.pub_date = timezone.now()
        self.edit_date = timezone.now()
        self.save() 
        
    def __unicode__(self):
        s = 'U: %s %s and comment: %s' % (self.user, self.user.id, self.comment_text)
        # s += str(self.comment_text)
        return s


