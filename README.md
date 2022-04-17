# AWS Lex V2 - An Online Shop Order Chatbot
CS4296 group 8
## Chatbot Conversation Flow

## Architecture
![image](https://user-images.githubusercontent.com/43038654/163716844-1bcb1e32-533d-486b-809f-18e67bfc7f6a.png)
## Amazon Lex V2
- Import Chatbot
  1. Compress OnlineShopChatbot Directory as **OnlineShopChatbot.zip**
  2. Login to **AWS console** with a valid account
  3. Navigate to Services and search for **Amazon Lex**
  4. Click get started
  5. Under the bots section, click **Action, Import**
  6. Input file section:
      - Bot name: **OnlineShopChatbot**
      - Input file: **OnlineShopChatbot.zip**
      - Password: N/A
  7. IAM permission section:
      - Runtime role: **Create a role with basic Amazon Lex permissions.**
  8. Children's Online Privacy Protection Act (COPPA)
      - Is use of your bot subject to the Children's Online Privacy Protection Act (COPPA)? **No**
  9. Idle session timeout
      - Session timeout: **5 minute(s)**
  10. Advanced settings - optional: N/A
  11. Navigate to the Bots section, imported bot status should be **Available**.
## AWS Lambda function
## Lex & Lambda Integration
(AWS console) Amazon Lex -> Bots -> OnlineShopChatbot -> Aliases -> prod -> Languages -> English -> Lambda function :

    Source : productinformation
    Lambda function version or alias : $LATEST
## Amazon DynamoDB
