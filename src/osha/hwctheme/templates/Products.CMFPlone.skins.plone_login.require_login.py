## Script (Python) "require_login"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Login

login = 'login'
language = context.portal_languages.getPreferredLanguage()

portal = context.portal_url.getPortalObject()
# if cookie crumbler did a traverse instead of a redirect,
# this would be the way to get the value of came_from
#url = portal.getCurrentUrl()
#context.REQUEST.set('came_from', url)

if context.portal_membership.isAnonymousUser():
    root = portal.restrictedTraverse(language)
    return root.restrictedTraverse(login)()
else:
    return portal.restrictedTraverse('insufficient_privileges')()
