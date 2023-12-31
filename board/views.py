from django.shortcuts import render, redirect, get_object_or_404
from .forms import BoardWriteForm, CommentWriteForm
from .models import Board
from user.models import User
from user.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, ValidationError

def board_list(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session': login_session }

    normal_boards = Board.objects.filter(board_name='normal')
    question_boards = Board.objects.filter(board_name='question')
    introduce_boards = Board.objects.filter(board_name='introduce')
    recommend_boards = Board.objects.filter(board_name='recommend')

    context['normal_boards'] = normal_boards
    context['question_boards'] = question_boards
    context['introduce_boards'] = introduce_boards
    context['recommend_boards'] = recommend_boards

    return render(request, 'board/board_list.html', context)

@login_required
def board_write(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session': login_session }

    if request.method == 'GET':
        write_form = BoardWriteForm()
        context['forms'] = write_form
        return render(request, 'board/board_write.html', context)
    
    elif request.method == 'POST':
        write_form = BoardWriteForm(request.POST)

        if write_form.is_valid():
            writer = User.objects.get(user_id=login_session)
            board = Board(
                title=write_form.title,
                contents=write_form.contents,
                writer=writer,
                board_name=write_form.board_name
            )
            board.save()
            return redirect('/board')
        else:
            context['forms'] = write_form
            if write_form.errors:
                for value in write_form.errors.values():
                    context['error'] = value
            return render(request, 'board/board_write.html', context)

def board_detail(request, pk):
    login_session = request.session.get('login_session', '')
    context = { 'login_session': login_session }

    board = get_object_or_404(Board, id=pk)
    context['board'] = board

    board.hits += 1
    board.save()

    if board.writer.user_id == login_session:
        context['writer'] = True
    else:
        context['writer'] = False

    return render(request, 'board/board_detail.html', context)

def board_delete(request, pk):
    login_session = request.session.get('login_session', '')
    board = get_object_or_404(Board, id=pk)
    if board.writer.user_id == login_session:
        board.delete()
        return redirect('/board')
    else:
        return redirect(f'/board/detail/{pk}/')

def board_update(request, pk):
    login_session = request.session.get('login_session', '')
    context = { 'login_session': login_session }

    board = get_object_or_404(Board, id=pk)
    context['board'] = board

    if board.writer.user_id != login_session:
        return redirect(f'/board/detail/{pk}/')

    if request.method == 'GET':
        write_form = BoardWriteForm(instance=board)
        context['forms'] = write_form
        return render(request, 'board/board_update.html', context)
    
    elif request.method == 'POST':
        write_form = BoardWriteForm(request.POST)

        if write_form.is_valid():

            board.title=write_form.title
            board.contents=write_form.contents
            board.board_name=write_form.board_name

            board.save()
            return redirect('/board')
        else:
            context['forms'] = write_form
            if write_form.errors:
                for value in write_form.errors.values():
                    context['error'] = value
            return render(request, 'board/board_update.html', context)

def comment_write(request, pk):
    login_session = request.session.get('login_session', '')
    context = { 'login_session': login_session }

    comment = get_object_or_404(Board, pk=pk)
    comment_form = CommentWriteForm(request.POST)
    if comment_form.is_valid():
        writer = User.objects.get(user_id=login_session)
        comment = Comment(
            contents = comment_form,
            writer=writer
        )
        comment.save()
        context = {
            "title": "Board",
            'post_id': pk,
            'comments': post.comment_set.all(),
            'comment_form': form,
        }
        return render(request, 'blog/post_detail.html', context)
    else:
        pass






