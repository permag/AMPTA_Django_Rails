class ChangeLimitPasswordUsersTable < ActiveRecord::Migration
  def change
    change_column :users, :hashed_password, :string, :limit => 70
  end
end
