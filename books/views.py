from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import *
from .models import Book


# Create your views here.

class BookView(View):
    def get(self, request):
        books = Book.objects.all().order_by("id")
        search_book = request.GET.get('q', "")
        if search_book:
            books = books.filter(title__icontains=search_book)
        page_size = request.GET.get('page_size', 2)
        paginator = Paginator(books, page_size)

        page_num = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_num)
        return render(request, 'books/list.html', {'page_obj': page_obj, "search_book": search_book})

class BookDetailView(View):
    def get(self, request, pk):
        book_detail = Book.objects.get(id=pk)
        review_form = BookReviewForm()
        return render(request, 'books/book_detail.html', {'book': book_detail, 'review_form': review_form})


class AddReviewVIEW(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = Book.objects.get(id=pk)
        review_form = BookReviewForm(data=request.POST)

        if review_form.is_valid():
            BookReview.objects.create(
                book=book,
                user=request.user,
                stars_given=review_form.cleaned_data['stars_given'],
                comment=review_form.cleaned_data['comment']
            )
            return redirect(reverse("books:detail", kwargs={"pk": book.id}))
        else:

            return render(request, 'books/book_detail.html', {'book': book, 'review_form': review_form})


class EditReviewVIEW(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        review_form = BookReviewForm(instance=review)
        return render(request, 'books/edit_review.html', {"book": book, "review": review, "review_form": review_form})

    def post(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        review_form = BookReviewForm(data=request.POST, instance=review)

        if review_form.is_valid():
            review_form.save()
            return redirect(reverse("books:detail", kwargs={"pk": book.id}))

        return render(request, 'books/edit_review.html', {"book": book, "review": review, "review_form": review_form})


class ConfirmDeleteReviewVIEW(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        return render(request, 'books/confirm_delete_review.html', {"book": book, "review": review})


class DeleteReviewVIEW(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)

        review.delete()

        messages.success(request, "You have successfully delete this review")
        return redirect(reverse("books:detail", kwargs={"pk": book.id}))
