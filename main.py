import os
from postai.social_poster import SocialPoster
from postai.model_serving import ModelServing

def main():
    # Define configuration
    system_prompt = """You are a social media content specialist with expertise in matching writing styles and voice across platforms. Your task is to:
    1. Analyze the provided example post(s) by examining:
       - Writing style, tone, and voice
       - Sentence structure and length
       - Use of hashtags, emojis, and formatting
       - Engagement techniques and calls-to-action
    2. Generate a new LinkedIn post about the given topic that matches:
       - The identified writing style and tone
       - Similar structure and formatting choices
       - Equivalent use of platform features and hashtags
       - Comparable engagement elements
    3. Return only the generated post, formatted exactly as it would appear on LinkedIn, without any additional commentary or explanations."""

    prompt_template = """
    example posts:
    {example_posts}
    context:
    {context}
    additional instructions:
    {additional_instructions}
    """

    config = {
        "system_prompt": system_prompt,
        "prompt_template": prompt_template,
        "model_provider": "google",
        "model_name": "gemini-2.0-flash-exp",
    }

    # Instantiate the custom model
    model = SocialPoster(config)

    # Log the model
    # model_info = model.log_and_register_model("social_poster", "src/social_poster.py")

    # # Set environment variables
    # os.environ["GEMINI_API_KEY"] = "your_gemini_api_key"
    # os.environ["MLFLOW_TRACING_ENABLED"] = "true"

    # # Initialize Model Serving
    # endpoint_name = "social-ai-staging"
    # model_server = ModelServing(
    #     model_name="mlflow_lightening_session.dev.social-ai-staging",
    #     endpoint_name=endpoint_name,
    # )
    # model_server.deploy_or_update_serving_endpoint()

if __name__ == "__main__":
    main()
