from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse

# Create your views here.

class Index(View):
    def get(self, request):
        post_objs = Post.objects.all()
        context = {
            "posts" : post_objs
        }
        return render(request, 'blog/board.html', context)

class List(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class Write(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:list')

    def write(request):
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save()
                return redirect('blog:list')

        form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form})

class Update(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'content']
    # success_url = reverse_lazy('blog:list')
    
    # intial 기능 사용 -> form에 값을 미리 넣어주기 위해서
    def get_initial(self):
        initial = super().get_initial() # UpdateView(generic view)에서 제공하는 initial(딕셔너리)
        post = self.get_object() # pk 기반으로 객체를 가져옴
        initial['title'] = post.title
        initial['content'] = post.content
        return initial
    
    def get_success_url(self): # get_absolute_url
        post = self.get_object() # pk 기반으로 현재 객체 가져오기
        return reverse('blog:detail', kwargs={ 'pk': post.pk })

class Delete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')

class DetailView(View):
    def get(self, request, pk): # post_id: 데이터베이스 post_id
        # list -> object 상세 페이지 -> 상세 페이지 하나의 내용
        # pk 값을 왔다갔다, 하나의 인자
        
        # 데이터베이스 방문
        # 해당 글
        # 장고 ORM (pk: 무조건 pk로 작성해야한다.)
        post = Post.objects.get(pk=pk)
        # 댓글
        comments = Comment.objects.filter(post=post)
        # 해시태그
        # hashtags = HashTag.objects.filter(post=post)
        
        # 댓글 Form
        comment_form = CommentForm()
        
        # 태그 Form
        # hashtag_form = HashTagForm()
        
        context = {
            'post': post,
            'comments': comments,
            # 'hashtags': hashtags,
            'comment_form': comment_form,
            # 'hashtag_form': hashtag_form
        }
        
        return render(request, 'blog/post_detail.html', context)

### Comment
class CommentWrite(View):
    # def get(self, request):
    #     pass
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            # 사용자에게 댓글 내용을 받아옴
            content = form.cleaned_data['content']
            # 해당 아이디에 해당하는 글 불러옴
            post = Post.objects.get(pk=pk)
            # 댓글 객체 생성, create 메서드를 사용할 때는 save 필요 없음
            comment = Comment.objects.create(post=post, content=content)
            # comment = Comment(post=post) -> comment.save()
            return redirect('blog:detail', pk=pk)


class CommentDelete(View):
    def post(self, request, pk):
        # 지울 객체를 찾아야 한다. -> 댓글 객체
        comment = Comment.objects.get(pk=pk)
        # 상세페이지로 돌아가기
        post_id = comment.post.id
        # 삭제
        comment.delete()
        
        return redirect('blog:detail', pk=post_id)