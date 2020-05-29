from django.shortcuts import redirect, reverse, render
from django.db.models import Q
from django.http import Http404
from django.views.generic import View
from users import models as user_models
from reservations import models as reservation_models
from . import models, forms


def go_conversation(request, host_pk, guest_pk):
    user_host = user_models.User.objects.get_or_none(pk=host_pk)
    user_guest = user_models.User.objects.get_or_none(pk=guest_pk)
    # reservation = reservation_models.Reservation.obejcts.get_or_none()
    if user_host is not None and user_guest is not None:
        try:
            # conversation = models.Conversation.objects.get(
            #     Q(participants=user_host) & Q(participants=user_guest)
            # )
            # ojects.filter(participants=user_host).filter(participants=user_guest) 이렇게 찾을 수도 있음
            conversation = (
                models.Conversation.objects.filter(participants__pk=host_pk)
                & models.Conversation.objects.filter(participants__pk=guest_pk)
            ).first()
            if conversation is None:
                print("없음")
                raise models.Conversation.DoesNotExist
        except models.Conversation.DoesNotExist:
            print("예외처리됨")
            conversation = models.Conversation.objects.create()
            conversation.participants.add(user_host, user_guest)
            print(conversation)
            # print(conversation.participants.all())
    print(conversation)
    return redirect(reverse("conversations:detail", kwargs={"pk": conversation.pk}))


class ConversationDetailView(View):
    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        conversation = models.Conversation.objects.get_or_none(pk=pk)
        if not conversation:
            raise Http404()
        return render(
            self.request,
            "conversations/conversation_detail.html",
            {"conversation": conversation},
        )

    def post(self, *args, **kwargs):
        message = self.request.POST.get("message", None)
        pk = kwargs.get("pk")
        conversation = models.Conversation.objects.get_or_none(pk=pk)
        if not conversation:
            raise Http404()

        if message is not None:
            models.Message.objects.create(
                message=message, user=self.request.user, conversation=conversation
            )
        return redirect(reverse("conversations:detail", kwargs={"pk": pk}))
