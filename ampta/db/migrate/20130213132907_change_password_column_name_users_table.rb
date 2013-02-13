class ChangePasswordColumnNameUsersTable < ActiveRecord::Migration
  def change
    rename_column :users, :password, :hashed_password
  end
end
