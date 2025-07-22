import os
from animatediff.inference import run_inference

def generate_animation(prompt, output_dir="results", motion_module_path="models/Motion_Module", base_model_path="models/StableDiffusion"):
    os.makedirs(output_dir, exist_ok=True)

    run_inference(
        prompt=prompt,
        motion_module_path=motion_module_path,
        base_model_path=base_model_path,
        output_dir=output_dir,
        num_frames=24,
        guidance_scale=7.5,
        width=512,
        height=512,
        steps=25,
        fps=8,
        seed=42
    )

if __name__ == "__main__":
    user_prompt = input("🎤 Enter your animation prompt: ")
    generate_animation(user_prompt)
    print("✅ Animation generation complete! Check the 'results/' folder.")
