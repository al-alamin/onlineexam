from django.contrib import admin

# Register your models here.
from .models import *
from .forms import *

from admin_method import *


class Upload_Question_From_Excel_Admin(admin.ModelAdmin):
    review_template = 'exam/excelparsing.html'
    exclude = ('pub_date', 'edit_date')
    form = Upload_Question_Set_From_Excel_Form

    # raw_id_fields = ('content',)


    def save_model(self, request, obj, form, change):
        print ("*****in excel save method")
        print (obj)
		# form = ExcelForm(request.POST, request.FILES)
        print ("\n this is a post method \n")




class Upload_Question_Set_From_Excel_Admin(admin.ModelAdmin):
    review_template = 'exam/excelparsing.html'
    exclude = ('pub_date', 'edit_date')
    form = Upload_Question_Set_From_Excel_Form
    raw_id_fields = ('question_set',)


    def save_model(self, request, obj, form, change):
        print ("\n\n************ upload excel question set\n")

        question_set = obj.question_set
        excel_file = obj.excel_file

        wb = openpyxl.load_workbook(excel_file)
        sheet = wb.get_sheet_by_name('Sheet1')

        mcq_list = []

        for row in range(10, 10000):
            if ((sheet.cell(row=row, column=1).value) is None):
                print ("in if part: " + str(sheet.cell(row=row, column=1).value))
                break
            q = create_mcq_from_excel(request, sheet, row, question_set)

            if (not q):
                break

            # print (q)

            mcq_list.append(q)

            # if (question_set):
            #     # q.tag_content = str(content)
            #     question_set.mcq_question.add(q)

            


            # q.save()

            # # question_set.individual_mcq_marks = marks
            # # question_set.negative_marking_percentage = negative_marks  
            # question_set.save()

            # t3 = str(sheet.cell(row=row, column=9).value)






        print(mcq_list)
        func()
        ret = save_mcq(request, mcq_list, question_set)
        
        obj.save()

        if (ret):
            messages.add_message(request, messages.INFO, '%s MCQ Question Has Been Added To The Question Set' % ret)













class Upload_Quick_Question_From_Excel_Admin(admin.ModelAdmin):
    # review_template = 'exam/excelparsing.html'
    exclude = ('pub_date', 'edit_date')
    form = Upload_Quick_Question_From_Excel_Form
    raw_id_fields = ('reading_content',)


    def save_model(self, request, obj, form, change):
        print ("\n\n************ quick question \n")
        # question_set = obj.question_set
        # excel_file = obj.excel_file


        reading_content = obj.reading_content
        excel_file = obj.excel_file

        wb = openpyxl.load_workbook(excel_file)
        sheet = wb.get_sheet_by_name('Sheet1')

        quick_question_list = []

        for row in range(10, 10000):
            if ((sheet.cell(row=row, column=1).value) is None):
                # print ("in if part: " + str(sheet.cell(row=row, column=1).value))
                break
            q = create_quick_question_from_excel(request, sheet, row, reading_content)

            if (not q):
                break

            # print (q)

            quick_question_list.append(q)

        ret = save_quick_question(request, quick_question_list, reading_content)
        
        # obj.save()

        if (ret):
            messages.add_message(request, messages.INFO, '%s Quick Question Has Been Added To The Question Set' % ret)


        obj.save()






# admin.site.register(Upload_Question_From_Excel, Upload_Question_From_Excel_Admin)
admin.site.register(Upload_Question_Set_From_Excel, Upload_Question_Set_From_Excel_Admin)

admin.site.register(Upload_Quick_Question_From_Excel, Upload_Quick_Question_From_Excel_Admin)








