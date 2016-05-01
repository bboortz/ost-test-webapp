#!/usr/bin/env python

import os
import keystoneclient.client as ksclient
import glanceclient.client as glclient


class OpenStackClient:

	def __init__(self):
		self.keystone = None
		self.glance = None

	def keystone_get_credentials(self):
		d = {}
		d['username'] = os.environ['OS_USERNAME']
		d['password'] = os.environ['OS_PASSWORD']
		d['auth_url'] = os.environ['OS_AUTH_URL']
		d['tenant_name'] = os.environ['OS_TENANT_NAME']
		return d

	def keystone_authenticate(self):
		creds = self.keystone_get_credentials() 
		self.keystone = ksclient.Client( **creds )

	def glance_authenticate(self):
		if (self.keystone == None):
			self.keystone_authenticate()

		glance_endpoint = self.keystone.service_catalog.url_for(service_type='image', endpoint_type='publicURL')
		glance = glclient.Client(glance_endpoint, token=keystone.auth_token)

	def glance_list_images()
		return glance.images.list()


		except timeout as e:
			raise RestClientErr("timeout: %s" %e)

		return response
		

