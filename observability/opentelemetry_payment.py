from opentelemetry import trace, baggage
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, OTLPSpanExporter
from opentelemetry.trace import set_span_in_context
from opentelemetry.sdk.trace.export import ConsoleSpanExporter

# Setup OTEL
trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({SERVICE_NAME: "payment-service"})
    )
)
tracer = trace.get_tracer(__name__)
span_processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True))
trace.get_tracer_provider().add_span_processor(span_processor)

def process_payment(user_id):
    ctx = baggage.set_baggage("user_id", user_id)
    with tracer.start_as_current_span("process_payment", context=ctx) as span:
        span.set_attribute("payment_method", "credit_card")
        # your logic here
        print("Processing payment for:", user_id)
