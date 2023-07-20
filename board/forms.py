from django import forms
from .models import Board, Comment
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget

class BoardWriteForm(forms.ModelForm):
    title = forms.CharField(
        label='글 제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '게시글 제목'
            }),
        required=True,
    )

    contents = SummernoteTextField()

    options = (
        ('normal', '일반'),
        ('question', '질문'),
        ('introduce', '가입인사'),
        ('recommend', '추천')
    )

    board_name = forms.ChoiceField(
        label='게시판 선택',
        widget=forms.Select(),
        choices=options
    )

    field_order = [
        'title',
        'board_name',
        'contents'
    ]

    class Meta:
        model = Board
        fields = [
            'title',
            'contents',
            'board_name'
        ]
        widgets = {
            'contents' : SummernoteWidget()
        }
    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title', '')
        contents = cleaned_data.get('contents', '')
        board_name = cleaned_data.get('board_name', 'normal')

        if title == '':
            self.add_error('title', '글 제목을 입력하세요')
        elif contents == '':
            self.add_error('contents', '글 내용을 입력하세요')
        else:
            self.title = title
            self.contents = contents
            self.board_name = board_name


class CommentWriteForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['contents']
        widgets = {
            'contents': forms.Textarea(attrs={'rows': '3', 'cols': '35'})
        }
