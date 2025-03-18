# Use official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Train the model before running predictions
RUN python train_model.py

# Expose port (if needed for an API)
EXPOSE 5000

# Command to run the prediction script
CMD ["python", "predict.py"]
