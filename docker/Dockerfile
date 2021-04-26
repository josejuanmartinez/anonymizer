FROM aptplatforms/oraclelinux-python

WORKDIR /opt/anonymizer
RUN pwd
# Add all files from host to container
COPY ./ ./


# Install requirements
RUN yum groupinstall 'Development Tools'
RUN pip install --trusted-host github.com --trusted-host github-releases.githubusercontent.com -r requirements.txt

# Run AIOHTTP
CMD [ "python", "./main.py" ]
