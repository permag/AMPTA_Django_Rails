class CreateUsersProjects < ActiveRecord::Migration
  def up
    create_table :users_projects, :id => false do |t|
      t.integer :user_id
      t.integer :project_id
    end

    add_index :users_projects, [:user_id, :project_id]
  end

  def down
    drop_table :users_projects
  end
end
