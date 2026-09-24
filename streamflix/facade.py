
from .payments import PaymentProcessor
from .catalog import Video


class StreamingFacade:
    """
    Simplified entry point for the mobile/web client: it never talks to
    payment processors or videos directly, only to this facade.
    """

    def __init__(self, payment_processor: PaymentProcessor):
      self.payment_processor = payment_processor
      self.is_subscribed = False

    def subscribe(self, monthly_fee: float) -> str:
      charged = self.payment_processor.pay(monthly_fee)
      self.is_subscribed = True
      return charged

    def watch(self, video: Video) -> str:
      if not self.is_subscribed:
          raise PermissionError("subscription required")
      return video.play()
      pass
