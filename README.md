# ost-test-webapp
A web application to test the health of an OpenStack Cloud


# Test Cases
* try to reach API
* authenticate for API calls
* use the block storage
* use the blob/object storage
* different network tests
** try to reach service on localhost
** try to reach service on different host
** try to reach service on different tenant
** try to reach services on the internet
** try to reach services on the intranet



# Workflow

test-job --> test-webapp
         \> info-webapp
news-feed --> info-webapp
