from API.shared_vars import SharedVars
from API.mlx_api import MLX

vars = SharedVars
mlx2 = MLX(SharedVars)
mlx = MLX(SharedVars)

vars.workspace_id = 'hqwqwello'
vars.update_token('sdasdadadsaddsadsads')
print(mlx2.get_var('workspace_id'))
print(mlx.get_var('access_token'))