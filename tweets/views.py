from django.shortcuts import render, redirect
from .forms import TweetForm

def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)  # don't save to DB yet
            tweet.user = request.user        # assign the logged-in user
            tweet.save()
            return redirect('tweet_success') # redirect to success page
    else:
        form = TweetForm()
    return render(request, 'tweets/create_tweet.html', {'form': form})

def tweet_success(request):
    return render(request, 'tweets/success.html')

