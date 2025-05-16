
Transformers is designed to be fast and easy to use so that everyone can start learning or building with transformer models.
https://huggingface.co/docs/transformers/en/quicktour

This quickstart introduces you to Transformers’ key features and shows you how to:

load a pretrained model
run inference with Pipeline
fine-tune a model with Trainer

Stetup Steps : 
Create a User Access Token and log in to your account.

from huggingface_hub import notebook_login
notebook_login()

Step2 :

Install a machine learning framework.

!pip install torch 
!pip install tensorflow

Step3 :
Install Some additional libraries from the Hugging Face ecosystem for accessing datasets and vision models, evaluating training, and optimizing training for large models.

!pip install -U transformers datasets evaluate accelerate timm
