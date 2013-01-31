class RenameUsersProjectsTable < ActiveRecord::Migration
  def change
    rename_table :users_projects, :projects_users
  end
end
