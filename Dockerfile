FROM python:3.11-slim AS runner

WORKDIR /app

# Core environment configurations for clean terminal logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy ONLY the compiled python binaries from Stage 1
COPY --from=builder /root/.local /root/.local
# Copy your actual source code
COPY . .

# Inject the binaries folder directly into the container's execution path
ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000