from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from pustakalaya_apps.pustakalaya_account.models import UserProfile
from django.contrib.messages.views import SuccessMessageMixin
from pustakalaya_apps.document.models import Document
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from pustakalaya_apps.audio.models import Audio
from pustakalaya_apps.video.models import Video
from .forms import DocumentFileUploadForm, AudioFileUploadForm, VideoFileUploadForm


@login_required()
def dashboard(request):
    return render(request, "dashboard/dashboard_base.html")


def profile(request):
    """
    Render the user profile template
    :param request:
    :return:
    """
    return render(request, 'dashboard/profile.html', {
        "user": request.user
    })


def profile_edit(request):
    pass


class ProfileEdit(UpdateView):
    model = UserProfile
    fields = (
        "first_name",
        "last_name",
        "phone_no",
    )
    template_name = 'dashboard/profile/profile.html'


class AddDocumentView(CreateView):
    model = Document
    fields = [
                'title',
                'collections',
                'document_file_type',
                'languages',
                'document_interactivity',
                'publisher',
                'keywords',
                'document_series',
                'document_type',
                'license_type'
            ]

    template_name = "dashboard/document/document_add.html/"
    success_url = reverse_lazy("dashboard:profile")

    def clean(self, AddDocumentView):
        cleaned_data = super(AddDocumentView, self).clean()
        title = cleaned_data.get('title')
        collections = cleaned_data.get('collections')
        document_file_type = cleaned_data.get('document_file_type')
        languages = cleaned_data.get('languages')
        document_interactivity = cleaned_data.get('document_interactivity')
        publisher = cleaned_data.get('publisher')
        keywords = cleaned_data.get('keywords')
        document_series = cleaned_data.get('document_series')
        document_type = cleaned_data.get('document_type')
        license_type = cleaned_data.get('license_type')

        if not title and not collections and not document_file_type and not languages and not document_interactivity and not publisher and not keywords and not document_series and not document_type and not license_type:
            raise cleaned_data.ValidationError('You have to write something!')

    def get_context_data(self, **kwargs):
        context = super(AddDocumentView, self).get_context_data(**kwargs)
        if self.request.POST:
            file_upload_form = DocumentFileUploadForm(self.request.POST)
            if file_upload_form.is_valid():
                file_upload_form.save()

            context['document_file_upload_form'] = DocumentFileUploadForm(self.request.POST)
        else:
            context['document_file_upload_form'] = DocumentFileUploadForm()

        return context


class UpdateDocumentView(SuccessMessageMixin, UpdateView):
    model = Document
    fields = [
                'title',
                'collections',
                'document_file_type',
                'languages',
                'document_interactivity',
                'publisher',
                'keywords',
                'document_series',
                'document_type',
                'license_type'
    ]

    template_name = "dashboard/document/document_edit.html/"
    success_url = 'dashboard/document/document_edit.html/'
    success_message = "was update successfully !!"
    success_url = reverse_lazy("dashboard:profile")

    def clean(self, UpdateDocument):
        cleaned_data = super(UpdateDocument, self).clean()
        title = cleaned_data.get('title')
        collections = cleaned_data.get('collections')
        document_file_type = cleaned_data.get('document_file_type')
        languages = cleaned_data.get('languages')
        document_interactivity = cleaned_data.get('document_interactivity')
        publisher = cleaned_data.get('publisher')
        keywords = cleaned_data.get('keywords')
        document_series = cleaned_data.get('document_series')
        document_type = cleaned_data.get('document_type')
        license_type = cleaned_data.get('license_type')
        form_class = DocumentFileUploadForm()

        if not title and not collections and not document_file_type and not languages and not document_interactivity and not publisher and not keywords and not document_series and not document_type and not license_type:
            raise cleaned_data.ValidationError('You have to write something!')


class DeleteDocumentView(SuccessMessageMixin, DeleteView):
    model = Document
    fields = [
                'title',
                'collections',
                'document_file_type',
                'languages',
                'document_interactivity',
                'publisher',
                'keywords',
                'document_series',
                'document_type',
                'license_type'
    ]

    template_name = "dashboard/document/document_delete.html/"
    success_url = '/'
    success_message = "was deleted successfully"


class AddAudioView(CreateView):
    model = Audio
    fields = [
                'title',
                'collections',
                'education_levels',
                'languages',
                'publisher',
                'audio_types',
                'audio_read_by',
                'audio_genre',
                'keywords',
                'audio_series',
                'license_type'
    ]

    template_name = "dashboard/audio/audio_add.html/"
    success_url = reverse_lazy("dashboard:profile")

    def clean(self, AddAudioView):
        cleaned_data = super(AddAudioView, self).clean()
        title = cleaned_data.get('title')
        collections = cleaned_data.get('collections')
        education_levels = cleaned_data.get('education_levels')
        languages = cleaned_data.get('languages')
        audio_types = cleaned_data.get('audio_types')
        publisher = cleaned_data.get('publisher')
        audio_types = cleaned_data.get('audio_types')
        audio_read_by = cleaned_data.get('audio_read_by')
        audio_genre = cleaned_data.get('audio_genre')
        keywords = cleaned_data.get('keywords')
        audio_series = cleaned_data.get('audio_series')
        license_type = cleaned_data.get('license_type')

        if not title and not collections and not education_levels and not languages and not \
            audio_types and not publisher and not audio_types and not keywords and not audio_read_by \
            and not audio_genre and not audio_series and not license_type:
            raise cleaned_data.ValidationError('You have to write something!')

    def get_context_data(self, **kwargs):
        context = super(AddAudioView, self).get_context_data(**kwargs)
        if self.request.POST:
            file_upload_form = AudioFileUploadForm(self.request.POST)
            if file_upload_form.is_valid():
                file_upload_form.save()

            context['audio_file_upload_form'] = AudioFileUploadForm(self.request.POST)
        else:
            context['audio_file_upload_form'] = AudioFileUploadForm()

        return context


class UpdateAudioView(UpdateView):
    model = Audio
    fields = [
                'title',
                'collections',
                'education_levels',
                'languages',
                'publisher',
                'audio_types',
                'audio_read_by',
                'audio_genre',
                'keywords',
                'audio_series',
                'license_type'
    ]

    template_name = "dashboard/audio/audio_edit.html/"
    success_url = reverse_lazy("dashboard:profile")

    def clean(self, UpdateAudioView):
        cleaned_data = super(UpdateAudioView, self).clean()
        title = cleaned_data.get('title')
        collections = cleaned_data.get('collections')
        education_levels = cleaned_data.get('education_levels')
        languages = cleaned_data.get('languages')
        audio_types = cleaned_data.get('audio_types')
        publisher = cleaned_data.get('publisher')
        audio_types = cleaned_data.get('audio_types')
        audio_read_by = cleaned_data.get('audio_read_by')
        audio_genre = cleaned_data.get('audio_genre')
        keywords = cleaned_data.get('keywords')
        audio_series = cleaned_data.get('audio_series')
        license_type = cleaned_data.get('license_type')

        if not title and not collections and not education_levels and not languages and not \
            audio_types and not publisher and not audio_types and not keywords and not audio_read_by \
            and not audio_genre and not audio_series and not license_type:
            raise cleaned_data.ValidationError('You have to write something!')


class DeleteAudioView(SuccessMessageMixin, DeleteView):
    model = Audio
    fields = [
                'title',
                'collections',
                'education_levels',
                'languages',
                'publisher',
                'audio_types',
                'audio_read_by',
                'audio_genre',
                'keywords',
                'audio_series',
                'license_type'
    ]

    template_name = "dashboard/audio/audio_delete.html/"
    success_url = 'dashboard:profile'
    success_message = "was deleted successfully"


class AddVideoView(CreateView):
    model = Video
    fields = [
                'title',
                'collections',
                'education_levels',
                'languages',
                'publisher',
                'video_director',
                'video_genre',
                'keywords',
                'video_series',
                'license_type'
    ]

    template_name = "dashboard/video/video_add.html/"
    success_url = reverse_lazy("dashboard:profile")

    def clean(self, AddVideoView):
        cleaned_data = super(AddVideoView, self).clean()
        title = cleaned_data.get('title')
        collections = cleaned_data.get('collections')
        education_levels = cleaned_data.get('education_levels')
        languages = cleaned_data.get('languages')
        publisher = cleaned_data.get('publisher')
        video_director = cleaned_data.get('video_director')
        video_genre = cleaned_data.get('video_genre')
        keywords = cleaned_data.get('keywords')
        video_series = cleaned_data.get('video_series')
        license_type = cleaned_data.get('license_type')

        if not title and not collections and not education_levels and not languages and not video_director and not video_genre and not publisher and not keywords and not video_series and not license_type:
            raise cleaned_data.ValidationError('You have to write something!')

    def get_context_data(self, **kwargs):
        context = super(AddVideoView, self).get_context_data(**kwargs)
        if self.request.POST:
            file_upload_form = VideoFileUploadForm(self.request.POST)
            if file_upload_form.is_valid():
                file_upload_form.save()

            context['video_file_upload_form'] = VideoFileUploadForm(self.request.POST)
        else:
            context['video_file_upload_form'] = VideoFileUploadForm()

        return context


class UpdateVideoView(UpdateView):
    model = Video

    fields = [
                'title',
                'collections',
                'education_levels',
                'languages',
                'publisher',
                'video_director',
                'video_genre',
                'keywords',
                'video_series',
                'license_type'
    ]

    template_name = "dashboard/video/video_edit.html/"
    success_url = reverse_lazy("dashboard:profile")

    def clean(self, UpdateVideo):
        cleaned_data = super(UpdateVideo, self).clean()
        title = cleaned_data.get('title')
        collections = cleaned_data.get('collections')
        education_levels = cleaned_data.get('education_levels')
        languages = cleaned_data.get('languages')
        publisher = cleaned_data.get('publisher')
        video_director = cleaned_data.get('video_director')
        video_genre = cleaned_data.get('video_genre')
        keywords = cleaned_data.get('keywords')
        video_series = cleaned_data.get('video_series')
        license_type = cleaned_data.get('license_type')

        if not title and not collections and not education_levels and not languages and not video_director and not video_genre and not publisher and not keywords and not video_series and not license_type:
            raise cleaned_data.ValidationError('You have to write something!')


class DeleteVideoView(SuccessMessageMixin, DeleteView):
    model = Video

    fields = [
                'title',
                'collections',
                'education_levels',
                'languages',
                'publisher',
                'video_director',
                'video_genre',
                'keywords',
                'video_series',
                'license_type'
    ]

    template_name = "dashboard/video/video_delete.html/"
    success_url = 'dashboard:profile'
    success_message = "was deleted successfully"
