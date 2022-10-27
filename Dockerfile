ARG VERSION
FROM python:${VERSION} AS pybuilder
COPY requirements.txt /project/

WORKDIR /project
RUN pip install -r requirements.txt

FROM python:${VERSION}
ARG VERSION
ENV PYTHONPATH=/project/pkgs
COPY --from=pybuilder /usr/local/lib/python${VERSION}/site-packages /project/pkgs
COPY aiohttp_example.py /project/aiohttp_example.py

ENTRYPOINT ["python", "/project/aiohttp_example.py"]
