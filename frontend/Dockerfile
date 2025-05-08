# frontend/Dockerfile

# Stage 1: Build React app
FROM node:20-alpine AS build

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . . 
RUN npm run build  # produces a build/ directory with static files

# Stage 2: Serve with Nginx
FROM nginx:alpine
# Copy custom Nginx config for proxying /api requests
COPY nginx.conf /etc/nginx/conf.d/default.conf
# Copy React build output to Nginx's web root

COPY --from=build /app/dist /usr/share/nginx/html


# Expose port 80 for the web
EXPOSE 80

# Nginx will start by default via its entrypoint
