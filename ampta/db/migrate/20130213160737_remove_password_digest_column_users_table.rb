class RemovePasswordDigestColumnUsersTable < ActiveRecord::Migration
  def change
    remove_column :users, :password_digest
  end
end
