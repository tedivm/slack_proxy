# Slack Proxy

This extremely simple app solves a somewhat niche problem- letting your developers send notifications to Slack without having needing them to manage webhooks. You deploy this app inside your network and have them send their messages to it, and then it forwards it on to Slack and returns the response.

## Configuration

The `SLACK_WEBHOOK` environmental variable needs to be set.

## Sending Messages with the Slack Incoming Webhooks API

This proxy passes messages directly to the [Slack Incoming Webhooks API](https://api.slack.com/messaging/webhooks), without modification. The only thing developers have to do is point their request at this service instead of the `https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX` URL.


## Docker

This application can be found as a prebuild docker container on [docker hub](https://hub.docker.com/repository/docker/tedivm/slack_proxy).
