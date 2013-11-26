from pygit2 import clone_repository
from pygit2 import Repository
from pygit2 import GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE, GIT_CHECKOUT_SAFE_CREATE

def collectRepository(repo):
	repo_url = repo
	urlChunks = repo_url.split('/')
	repo_path = 'repos/' + urlChunks[len(urlChunks)-1].replace('.git', '').lower()

	if not os.path.exists(repo_path):
    repo = clone_repository(repo_url, repo_path)
   else:
   	print 'Repository ' + repo_path + ' already exists!'

	base = Repository(repo_path + '/.git')
	base.checkout('HEAD')
	
	return repo_path + '/.git'
